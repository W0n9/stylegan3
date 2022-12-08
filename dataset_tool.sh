#! /usr/bin/bash
###
 # @Author: TsungWing 38560218+W0n9@users.noreply.github.com
 # @Date: 2022-09-13 03:27:53
 # @LastEditors: TsungWing 38560218+W0n9@users.noreply.github.com
 # @LastEditTime: 2022-11-22 07:31:04
 # @FilePath: /stylegan3/dataset_tool.sh
 # @Description: 
 # 
 # Copyright (c) 2022 by TsungWing 38560218+W0n9@users.noreply.github.com, All Rights Reserved. 
### 

python dataset_tool.py --source=datasets/train/bulk_carrier --dest=datasets/train/bulk_carrier.zip --transform=resize-pad --resolution=256x256
python dataset_tool.py --source=datasets/train/cargo --dest=datasets/train/cargo.zip --transform=resize-pad --resolution=256x256
python dataset_tool.py --source=datasets/train/fishing --dest=datasets/train/fishing.zip --transform=resize-pad --resolution=256x256
python dataset_tool.py --source=datasets/train/other --dest=datasets/train/other.zip --transform=resize-pad --resolution=256x256
python dataset_tool.py --source=datasets/train/tanker --dest=datasets/train/tanker.zip --transform=resize-pad --resolution=256x256
# python dataset_tool.py --source=datasets/FUSAR_obb/bulk_carrier_v --dest=datasets/padding/bulk_carrier_v.zip --transform=resize-pad --resolution=256x256