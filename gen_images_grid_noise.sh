#! /usr/bin/zsh
###
 # @Author: TsungWing 38560218+W0n9@users.noreply.github.com
 # @Date: 2022-08-31 11:35:45
 # @LastEditors: TsungWing 38560218+W0n9@users.noreply.github.com
 # @LastEditTime: 2022-12-08 08:22:05
 # @FilePath: /stylegan3/gen_images_grid_noise.sh
 # @Description: Generate image grid for quality evaluation.
 # 
 # Copyright (c) 2022 by TsungWing 38560218+W0n9@users.noreply.github.com, All Rights Reserved. 
### 

CUDA_VISIBLE_DEVICES=1

network=/home/w0n9/stylegan3/training-runs/A30/00021-stylegan2-tanker-gpus4-batch64-gamma0.4096/network-snapshot-000161.pkl
seeds=0-479
noise=random
outdir=out/tanker

for class in `seq 0 1 4`
do
    for trunc in `seq 0 1 9`
    do
        python gen_images_grid.py --outdir=$outdir --trunc=0.$trunc --seeds=$seeds --class=$class --noise-mode=$noise --network=$network
    done

    for trunc in `seq 1 1 9`
    do
        python gen_images_grid.py --outdir=$outdir --trunc=-0.$trunc --seeds=$seeds --class=$class --noise-mode=$noise --network=$network
    done

    python gen_images_grid.py --outdir=$outdir --trunc=1 --seeds=$seeds --class=$class --noise-mode=$noise --network=$network

    python gen_images_grid.py --outdir=$outdir --trunc=-1 --seeds=$seeds --class=$class --noise-mode=$noise --network=$network
done