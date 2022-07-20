# A tool convert tiff to jpg
import os
from glob import glob

import imageio

while True:
    tifs = glob("*.tiff")

    if len(tifs) == 0:
        print("No tif found")
        break
    else:
        for tif in tifs:
            print(tif)
            img = imageio.imread(tif)
            imageio.imwrite(tif.replace(".tiff", ".jpg"), img, format="jpg")
            os.remove(tif)
            print("converted")
        break
