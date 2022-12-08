#! /usr/bin/zsh
###
 # @Author: TsungWing 38560218+W0n9@users.noreply.github.com
 # @Date: 2022-08-24 21:01:01
 # @LastEditors: TsungWing 38560218+W0n9@users.noreply.github.com
 # @LastEditTime: 2022-08-31 22:06:42
 # @FilePath: /stylegan3/gen_images_grid_uncond.sh
 # @Description: Generate image grid for quality evaluation.
 # 
 # Copyright (c) 2022 by TsungWing 38560218+W0n9@users.noreply.github.com, All Rights Reserved. 
### 

network=/home/w0n9/stylegan3/training-runs/A30/00021-stylegan2-tanker-gpus4-batch64-gamma0.4096/network-snapshot-000161.pkl
seeds=0-479
noise=const
outdir=out/tanker

for trunc in `seq 0 1 9`
do
    python gen_images_grid.py --outdir=$outdir --trunc=0.$trunc --seeds=$seeds --noise-mode=$noise --network=$network
done

for trunc in `seq 1 1 9`
do
    python gen_images_grid.py --outdir=$outdir --trunc=-0.$trunc --seeds=$seeds --noise-mode=$noise --network=$network
done

python gen_images_grid.py --outdir=$outdir --trunc=1 --seeds=$seeds --noise-mode=$noise --network=$network

python gen_images_grid.py --outdir=$outdir --trunc=-1 --seeds=$seeds --noise-mode=$noise --network=$network