"""

使用说明：
推荐使用图片的尺寸 340*340
边框尺寸 28
图片放在image文件夹下
加框图片生成在dataset文件夹下
边框颜色随机生成可自行修改

"""

import cv2 as cv
import os
import random






# 边框尺寸
frame_size = 28
number=0
if not (os.path.exists('./dataset')):#如果有没有dataset这个文件
    os.mkdir("./dataset")#创建这个文件

for curDir, dirs, files in os.walk("image", topdown=False):
    image = os.listdir(curDir)#返回指定文件夹包含的文件或文件夹的名字的列表
    curdir=os.path.split(curDir)[1]  #
    if not (os.path.exists('./dataset/%s' %curdir)):  # 如果有没有dataset这个文件
        os.mkdir("./dataset/%s" %curdir)  # 创建这个文件

    for i in image:
        number+=1
        try:

           img = cv.imread('./image/%s/%s' %(curdir ,i))
           cv.rectangle(img, (0, 0), (img.shape[1], img.shape[0]),
                     # 颜色改这里
                     (random.randint(0, 200),
                      random.randint(64, 255),
                      random.randint(64, 255)),
                     frame_size, 4)
           cv.imshow('Picture preview', img)
           cv.waitKey(200)
           cv.imwrite('./dataset/%s/%s' %(curdir,i), img)
        except:
           continue
