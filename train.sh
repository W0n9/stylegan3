#! /usr/bin/bash
###
 # @Author: TsungWing 38560218+W0n9@users.noreply.github.com
 # @Date: 2022-04-29 16:49:01
 # @LastEditors: TsungWing 38560218+W0n9@users.noreply.github.com
 # @LastEditTime: 2022-09-15 02:43:56
 # @FilePath: /stylegan3/train.sh
 # @Description: 
 # 
 # Copyright (c) 2022 by TsungWing 38560218+W0n9@users.noreply.github.com, All Rights Reserved. 
### 

# python train.py \
#     --outdir=training-runs \
#     --cfg=stylegan3-r \
#     --gpus=2 \
#     --batch=32 \
#     --gamma=2 \
#     --batch-gpu=8 \
#     --snap=20 \
#     --mirror=1 \
#     --cbase=16384 \
#     --dlr=0.0025 \
#     --metrics=fid50k_full,eqt50k_int,eqr50k \
#     --resume=pretrain/stylegan3-r-ffhqu-256x256.pkl \
#     --data=datasets/padding/fishing.zip

# CUDA_VISIBLE_DEVICES=0,1 \
#     python train.py \
#     --outdir=training-runs \
#     --cfg=stylegan2 \
#     --gpus=2 \
#     --batch=32 \
#     --gamma=0.4096 \
#     --map-depth=2 \
#     --glr=0.0025 \
#     --dlr=0.0025 \
#     --cbase=16384 \
#     --snap=20 \
#     --mirror=1 \
#     --metrics=fid50k_full\
#     --data=datasets/padding/bulk_carrier_v.zip

# CUDA_VISIBLE_DEVICES=0 \
#     python train.py \
#     --outdir=training-runs \
#     --cfg=stylegan3-t \
#     --gpus=1 \
#     --batch=32 \
#     --gamma=2 \
#     --batch-gpu=8 \
#     --snap=20 \
#     --cbase=16384 \
#     --dlr=0.0025 \
#     --metrics=fid50k_full,eqt50k_int,eqr50k \
#     --resume=pretrain/stylegan3-t-ffhqu-256x256.pkl \
#     --data=datasets/raw/bulk_carrier_raw.zip

# CUDA_VISIBLE_DEVICES=1 \
#     python train.py \
#     --outdir=training-runs \
#     --cfg=stylegan3-r \
#     --gpus=1 \
#     --batch=32 \
#     --gamma=2 \
#     --batch-gpu=8 \
#     --snap=20 \
#     --cbase=16384 \
#     --dlr=0.0025 \
#     --metrics=fid50k_full,eqt50k_int,eqr50k \
#     --resume=pretrain/stylegan3-r-ffhqu-256x256.pkl \
#     --data=datasets/raw/bulk_carrier_raw.zip

CUDA_VISIBLE_DEVICES=0,1 \
    python train.py \
    --outdir=training-runs \
    --cfg=stylegan2 \
    --gpus=2 \
    --batch=64 \
    --gamma=0.4096 \
    --map-depth=2 \
    --glr=0.0025 \
    --dlr=0.0025 \
    --cbase=16384 \
    --snap=5 \
    --mirror=1 \
    --kimg=300 \
    --metrics=fid50k_full,pr50k3_full \
    --resume=pretrain/stylegan2-ffhq-256x256.pkl \
    --data=datasets/padding/bulk_carrier_v.zip