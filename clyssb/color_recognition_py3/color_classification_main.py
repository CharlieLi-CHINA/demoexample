# -*- coding: utf-8 -*-
#----------------------------------------------
"""
fuction:基于knn的颜色识别
@author: liqilv
"""
from __future__ import division
import numpy as np
import cv2,time,sys,os
import knn_classifier
from PIL import Image  
from skimage import io
import color_histogram_feature_extraction
 
#checking whether the training data is ready
PATH='./training.data'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):  
    #如果path是一个存在的文件，返回True。否则返回False
    # os.R_OK来测试PATH是否可读
    print ("training data is ready, classifier is loading...")
else:
    print ("training data is being created...")
    open('training.data','w')
    color_histogram_feature_extraction.training()
    print ("training data is ready, classifier is loading...")

def cut_lower_half(img):
    #剪切图像
    x,y = img.size
    #box = [1,y/2,x,y]
    box = [x/10,y/2,9*x/10,2*y/3]
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
#pic_name.sort(key=lambda x:int(x[:-4]))
for i in range(0,len(pic_name)):
    picture_name= pic_name[i]
    
#批量读入图像并存在coll
#print pic_name
coll = io.ImageCollection("./test_picture/*.jpg")

print ('the mount of the picture is :',len(coll))

mount_all = len(coll)
mount = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,len(coll)):
    
    io.imsave('test1.jpg',coll[i])
    io.imsave('test2.jpg',coll[i])
    #print(coll[i])
    img1 = Image.open("test1.jpg")
    cut_lower_half(img1)
    frame = cv2.imread("linshi.jpg")
    pre_class = cv2.imread("test1.jpg")
    prediction = "n.a."
    frame2 =  cv2.imread("test2.jpg")
    color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    
    prediction = knn_classifier.main("training.data", "test.data")
    cv2.putText(frame2,  prediction, (15, 45 ), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),5)
    cv2.imshow('pre color',pre_class)
    #cv2.waitKey(0)&0xFF 
    cv2.imshow('color classifier',frame2)
    cv2.imwrite('./result_picture/' + picture_name[i],frame2)
    
    #用于统计正确率
    if prediction == "black":
        mount[0] = mount[0] + 1
    elif prediction == "gray":
        mount[1] = mount[1] + 1
    elif prediction == "white":
        mount[2] = mount[2] + 1
    elif prediction == "red":
        mount[3] = mount[3] + 1
    elif prediction == "yellow":
        mount[4] = mount[4] + 1
    elif prediction == "blue":
        mount[5] = mount[5] + 1
    elif prediction == "green":
        mount[6] = mount[6] + 1
    elif prediction == "purple":
        mount[7] = mount[7] + 1
    elif prediction == "pink":
        mount[8] = mount[8] + 1
    elif prediction == "brown":
        mount[9] = mount[9] + 1
    #statistics_most_ture(prediction)
    os.remove('test1.jpg')
    os.remove('test2.jpg')
    
    #识别结果写进去txt
    fp = open('./result_txt/test.txt','a+')
    fp.write(picture_name[i] + ' ' + prediction + '\n')
    fp.close()
    cv2.waitKey(0)&0xFF

#修改结果名字txt
result_txt_name = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
result_name = result_txt_name + '.txt'    

os.rename('./result_txt/test.txt', './result/'+ result_name)
mount_ture = max(mount)
ture_rate = float(mount_ture / mount_all)
str(ture_rate)
# print ("准确率：", ture_rate)
cv2.destroyAllWindows() 