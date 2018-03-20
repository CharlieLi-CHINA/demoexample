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

#cap = cv2.VideoCapture(0) #原来里面数值是1，结果运行不了，改成0后可以运行，可能是因为我用的是笔记本
#imagePath = './test_picture/0038636.jpg'
#cap = cv2.imread(imagePath)

#img1 = Image.open(imagePath)


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
"""
def statistics_most_ture(yuce):
    if yuce == "white":
        number_w = number_w +1
    elif yuce == "red":
        number_r = number_r +1
    elif yuce == "black":
        number_bl = number_bl +1    
    elif yuce == "blue":
        number_b = number_b +1
    elif yuce == "green":
        number_g = number_g +1
    elif yuce == "yellow":
        number_y = number_y +1    
    elif yuce == "brown":
        number_br = number_br +1
    elif yuce == "pink":
        number_p = number_p +1
    elif yuce == "violet":
        number_v = number_v +1
    elif yuce == "gray":
        number_gr = number_gr +1    
    elif yuce == "orange":
        number_0 = number_0r +1
        
    #most_number = 
"""
"""
def recognition():
    cut_lower_half(img1)
    cap = cv2.imread("./test_picture/linshi.jpg")
    frame = cap
    prediction = "n.a."
    color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    prediction = knn_classifier.main("training.data", "test.data")
"""    
#cut_lower_half(img1)

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
    if prediction == "brown":
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

#frame = cv2.imread("./test_picture/linshi.jpg")
#ret, frame = cap.read()
#frame = cap
#prediction = "n.a."

#color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    
#prediction = knn_classifier.main("training.data", "test.data")




"""
#显示结果
while(True):
    # Capture frame-by-frame
    #ret, frame = cap.read()
    color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    
    prediction = knn_classifier.main("training.data", "test.data")
    cap2 = cv2.imread(imagePath)
    frame2 = cap2
    cv2.putText(frame2, "Prediction: " + prediction, (15, 45), cv2.FONT_HERSHEY_PLAIN, 3, 200)

    # Display the resulting frame
    cv2.imshow('color classifier',frame2)

    #color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    
    #prediction = knn_classifier.main("training.data", "test.data")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
#cap.release()
cv2.destroyAllWindows()
"""


