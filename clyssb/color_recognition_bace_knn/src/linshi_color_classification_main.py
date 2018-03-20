# -*- coding: utf-8 -*-
#----------------------------------------------
#--- Author         : Ahmet Ozlu
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 31st December 2017 - new year eve :)
#----------------------------------------------
from __future__ import division
import cv2,time,sys
import color_histogram_feature_extraction
import knn_classifier
import os
import os.path
from PIL import Image
from skimage import io
import numpy as np


#checking whether the training data is ready
PATH='./training.data'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):  
    #如果path是一个存在的文件，返回True。否则返回False
    # os.R_OK来测试PATH是否可读
    print "training data is ready, classifier is loading..."
else:
    print "training data is being created..."
    open('training.data','w')
    color_histogram_feature_extraction.training()
    print "training data is ready, classifier is loading..."

def cut_lower_half(img):
    #剪切图像的下半部分
    x,y = img.size
    box = [1,y/2,x,y]
    img2 = img.crop(box)
    img2.save("linshi.jpg")
    
def file_name(file_dir):  
    pic_name= []
    for root, dirs, files in os.walk(file_dir):  
    #print(files) #当前路径下所有非目录子文件
        pic_name.append(files)
    return pic_name   

#用于批量处理
pic_name= file_name("./test_picture")#待识别图像文件名字的读取
for i in range(0,len(pic_name)):
    picture_name= pic_name[i]
    
#批量读入图像并存在coll
#print pic_name
coll = io.ImageCollection("./test_picture/*.jpg")

print 'the mount of the picture is :',len(coll)

mount_all = len(coll)
mount_ture = 0
for i in range(0,len(coll)):
    
    io.imsave('test.jpg',coll[i])
    img1 = Image.open("test.jpg")
    cut_lower_half(img1)
    frame = cv2.imread("linshi.jpg")
    prediction = "n.a."

    color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    
    prediction = knn_classifier.main("training.data", "test.data")
    if prediction == "red":
        mount_ture = mount_ture + 1
    #statistics_most_ture(prediction)
    os.remove('test.jpg')
    #print "全局变量YanSe",YanSe
    #识别结果写进去txt
    fp = open('./result/test.txt','a+')
    fp.write(picture_name[i] + ' ' + prediction + '\n')
    fp.close()
#修改结果名字txt
result_txt_name = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
result_name = result_txt_name + '.txt'    

os.rename('./result/test.txt', './result/'+ result_name)

ture_rate = float(mount_ture / mount_all)
str(ture_rate)
print "准确率：", ture_rate
