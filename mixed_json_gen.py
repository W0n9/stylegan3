'''
Author: lifuguan lifugan_10027@outlook.com
Date: 2022-11-27 17:29:39
LastEditors: lifuguan lifugan_10027@outlook.com
LastEditTime: 2022-11-27 20:04:32
FilePath: /stylegan3/mixed_json_gen.py
Description: 

Copyright (c) 2022 by lifuguan lifugan_10027@outlook.com, All Rights Reserved. 
'''

import os  
import json

category = {
    "bird":0,
    "cat":1,
    "cow":2,
    "horse":3,
    "sheep":4,
}

## 返回文件路径列表
def file_name(file_dir):   
    L=[]
    str="/"
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.png':  
                L.append([str.join(os.path.join(root, file).split("/")[-3:]),category[os.path.join(root, file).split("/")[-3]]])
    return L  

def metadata_dict(file_name):
    return {"labels":file_name}

if __name__ == "__main__":
    # print(file_name('datasets/lsun'))
    with open('metadata.json', 'w') as f:
        json.dump(metadata_dict(file_name('datasets/lsun')), f)