#! /usr/bin/zsh
###
 # @Author: TsungWing 38560218+W0n9@users.noreply.github.com
 # @Date: 2022-08-24 21:01:01
 # @LastEditors: TsungWing 38560218+W0n9@users.noreply.github.com
 # @LastEditTime: 2022-10-25 08:39:59
 # @FilePath: /stylegan3/gen_images.sh
 # @Description: Generate image grid for quality evaluation.
 # 
 # Copyright (c) 2022 by TsungWing 38560218+W0n9@users.noreply.github.com, All Rights Reserved. 
### 

network=training-runs/A30/00027-stylegan2-mixed_raw-gpus4-batch64-gamma0.2048/network-snapshot-004032.pkl
seeds=0-479
noise=random
outdir=out/mixed_raw

# for class in `seq 0 1 4`
# do
#     for trunc in `seq 0 1 9`
#     do
#         python gen_images.py --outdir=$outdir --trunc=0.$trunc --seeds=$seeds --class=$class --noise-mode=$noise --network=$network
#     done

#     for trunc in `seq 1 1 9`
#     do
#         python gen_images.py --outdir=$outdir --trunc=-0.$trunc --seeds=$seeds --class=$class --noise-mode=$noise --network=$network
#     done

#     python gen_images.py --outdir=$outdir --trunc=1 --seeds=$seeds --class=$class --noise-mode=$noise --network=$network

#     python gen_images.py --outdir=$outdir --trunc=-1 --seeds=$seeds --class=$class --noise-mode=$noise --network=$network
# done

for class in `seq 0 1 4`
do
    python gen_images.py --outdir=$outdir --trunc=1 --seeds=$seeds --class=$class --noise-mode=$noise --network=$network

    # python gen_images.py --outdir=$outdir --trunc=-1 --seeds=$seeds --class=$class --noise-mode=$noise --network=$network
done