'''
Author: TsungWing 38560218+W0n9@users.noreply.github.com
Date: 2022-11-28 00:37:34
LastEditors: TsungWing 38560218+W0n9@users.noreply.github.com
LastEditTime: 2022-12-08 08:23:34
FilePath: /stylegan3/mixed_json_gen.py
Description: mixed类型数据集的metadata生成

Copyright (c) 2022 by TsungWing 38560218+W0n9@users.noreply.github.com, All Rights Reserved. 
'''
"""
Author: TsungWing 38560218+W0n9@users.noreply.github.com
Date: 2022-11-28 00:37:34
LastEditors: TsungWing 38560218+W0n9@users.noreply.github.com
LastEditTime: 2022-11-28 00:37:56
FilePath: /stylegan3/mixed_json_gen.py
Description: 

Copyright (c) 2022 by TsungWing 38560218+W0n9@users.noreply.github.com, All Rights Reserved. 
"""
import os
import json

category = {
    "bird": 0,
    "cat": 1,
    "cow": 2,
    "horse": 3,
    "sheep": 4,
}

## 返回文件路径列表
def file_name(file_dir):
    L = []
    str = "/"
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == ".png":
                L.append(
                    [
                        str.join(os.path.join(root, file).split("/")[-3:]),
                        category[os.path.join(root, file).split("/")[-3]],
                    ]
                )
    return L


def metadata_dict(file_name):
    return {"labels": file_name}


if __name__ == "__main__":
    with open("metadata.json", "w") as f:
        json.dump(metadata_dict(file_name("datasets/lsun")), f)
