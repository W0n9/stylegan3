"""
Author: TsungWing 38560218+W0n9@users.noreply.github.com
Date: 2022-08-30 15:28:17
LastEditors: TsungWing 38560218+W0n9@users.noreply.github.com
LastEditTime: 2022-08-31 11:34:41
FilePath: /stylegan3/gen_images_grid.py
Description: Generate image grid using pretrained network pickle.

Copyright (c) 2022 by TsungWing 38560218+W0n9@users.noreply.github.com, All Rights Reserved. 
"""

import os
import re
from typing import List, Optional, Tuple, Union

import click
import dnnlib
import numpy as np
import PIL.Image
import torch

import legacy

# ----------------------------------------------------------------------------


def parse_range(s: Union[str, List]) -> List[int]:
    """Parse a comma separated list of numbers or ranges and return a list of ints.

    Example: '1,2,5-10' returns [1, 2, 5, 6, 7]
    """
    if isinstance(s, list):
        return s
    ranges = []
    range_re = re.compile(r"^(\d+)-(\d+)$")
    for p in s.split(","):
        m = range_re.match(p)
        if m:
            ranges.extend(range(int(m.group(1)), int(m.group(2)) + 1))
        else:
            ranges.append(int(p))
    return ranges


# ----------------------------------------------------------------------------


def parse_vec2(s: Union[str, Tuple[float, float]]) -> Tuple[float, float]:
    """Parse a floating point 2-vector of syntax 'a,b'.

    Example:
        '0,1' returns (0,1)
    """
    if isinstance(s, tuple):
        return s
    parts = s.split(",")
    if len(parts) == 2:
        return (float(parts[0]), float(parts[1]))
    raise ValueError(f"cannot parse 2-vector {s}")


# ----------------------------------------------------------------------------


def make_transform(translate: Tuple[float, float], angle: float):
    m = np.eye(3)
    s = np.sin(angle / 360.0 * np.pi * 2)
    c = np.cos(angle / 360.0 * np.pi * 2)
    m[0][0] = c
    m[0][1] = s
    m[0][2] = translate[0]
    m[1][0] = -s
    m[1][1] = c
    m[1][2] = translate[1]
    return m


# ----------------------------------------------------------------------------


@click.command()
@click.option("--network", "network_pkl", help="Network pickle filename", required=True)
@click.option(
    "--seeds",
    type=parse_range,
    help="List of random seeds (e.g., '0,1,4-6')",
    required=True,
)
@click.option(
    "--trunc",
    "truncation_psi",
    type=float,
    help="Truncation psi",
    default=1,
    show_default=True,
)
@click.option(
    "--class",
    "class_idx",
    type=int,
    help="Class label (unconditional if not specified)",
)
@click.option(
    "--noise-mode",
    help="Noise mode",
    type=click.Choice(["const", "random", "none"]),
    default="const",
    show_default=True,
)
@click.option(
    "--translate",
    help="Translate XY-coordinate (e.g. '0.3,1')",
    type=parse_vec2,
    default="0,0",
    show_default=True,
    metavar="VEC2",
)
@click.option(
    "--rotate",
    help="Rotation angle in degrees",
    type=float,
    default=0,
    show_default=True,
    metavar="ANGLE",
)
@click.option(
    "--outdir",
    help="Where to save the output images",
    type=str,
    required=True,
    metavar="DIR",
)
def generate_images_grid(
    network_pkl: str,
    seeds: List[int],
    truncation_psi: float,
    noise_mode: str,
    outdir: str,
    translate: Tuple[float, float],
    rotate: float,
    class_idx: Optional[int],
):
    """Generate images using pretrained network pickle."""

    print('Loading networks from "%s"...' % network_pkl)
    device = torch.device("cuda")
    with dnnlib.util.open_url(network_pkl) as f:
        G = legacy.load_network_pkl(f)["G_ema"].to(device)  # type: ignore

    os.makedirs(outdir, exist_ok=True)
    if class_idx is not None:
        os.makedirs(os.path.join(outdir, str(class_idx)), exist_ok=True)
    psi_filename = int(truncation_psi * 10)

    # Labels.
    label = torch.zeros([1, G.c_dim], device=device)
    if G.c_dim != 0:
        if class_idx is None:
            raise click.ClickException(
                "Must specify class label with --class when using a conditional network"
            )
        label[:, class_idx] = 1
    else:
        if class_idx is not None:
            print("warn: --class=lbl ignored when running on an unconditional network")

    # Generate images.

    for seed_idx, seed in enumerate(seeds):
        print("Generating image for seed %d (%d/%d) ..." % (seed, seed_idx, len(seeds)))
        z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)

        # Construct an inverse rotation/translation matrix and pass to the generator.  The
        # generator expects this matrix as an inverse to avoid potentially failing numerical
        # operations in the network.
        if hasattr(G.synthesis, "input"):
            m = make_transform(translate, rotate)
            m = np.linalg.inv(m)
            G.synthesis.input.transform.copy_(torch.from_numpy(m))

        img: torch.Tensor = G(
            z, label, truncation_psi=truncation_psi, noise_mode=noise_mode
        )
        img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)

        if seed_idx == 0:
            grid: np.array = img.cpu().numpy()
        else:
            grid = np.concatenate((grid, img.cpu().numpy()))

    if class_idx is None:
        save_image_grid(grid, f"{outdir}/{psi_filename}.jpg", (30, 16))
    else:
        save_image_grid(grid, f"{outdir}/{class_idx}/{psi_filename}.jpg", (30, 16))


# ----------------------------------------------------------------------------


def save_image_grid(img, fname, grid_size):
    # img = np.asarray(img, dtype=np.float32)
    # img = np.rint(img).clip(0, 255).astype(np.uint8)

    gw, gh = grid_size
    img = img.transpose(0, 3, 1, 2)
    _N, C, H, W = img.shape
    img = img.reshape([gh, gw, C, H, W])
    img = img.transpose(0, 3, 1, 4, 2)
    img = img.reshape([gh * H, gw * W, C])

    assert C in [1, 3]
    if C == 1:
        PIL.Image.fromarray(img[:, :, 0], "L").save(fname)
    if C == 3:
        PIL.Image.fromarray(img, "RGB").save(fname)


# ----------------------------------------------------------------------------

if __name__ == "__main__":
    generate_images_grid()  # pylint: disable=no-value-for-parameter

# ----------------------------------------------------------------------------
