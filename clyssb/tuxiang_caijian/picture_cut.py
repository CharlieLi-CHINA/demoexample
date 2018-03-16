#coding=utf-8
#
# 测试需要，裁剪图片，使用之前学过的技术
# 做一个裁剪的小案例

import os
#读取path路径下的 jpg文件
def getAllImages(path):
    #f.endswith（）  限制文件类型
    #f.endswith('.jpg')|f.endswith('.png')  改成这句可以读取jpg/png格式的文件
    #注意 返回的是绝对路径
   return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

import pylab as plb
import PIL.Image as Image
#循环读图
for path in getAllImages(r'D:\\Anaconda2\\liqilv\\clyssb\\tuxiang_caijian\\test'):
    #读图
    img = Image.open(path)
    #显示
    plb.imshow(img)
    #设置裁剪点（4个）
    corner = plb.ginput(4)
    #顺时针取点求解
    left = (corner[0][0] + corner[3][0])/2
    top = (corner[1][1] + corner[0][1])/2
    reight = (corner[1][0] + corner[2][0])/2
    under = (corner[3][1] + corner[2][1])/2
    #print left,top,reight,under
    #box = [left,top,reight,under]
    #box中的数必须是 int 否则会报错
    box = [int(left),int(top),int(reight),int(under)]
    #裁剪
    img2 = img.crop(box)
    #显示裁剪后的效果
    #plb.imshow(img2)
    #plb.show()
    #储存为原来路径覆盖原文件
    img2.save(path)
plb.show()