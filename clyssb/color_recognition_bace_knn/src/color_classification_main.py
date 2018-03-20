# -*- coding: utf-8 -*-
#----------------------------------------------
#--- Author         : Ahmet Ozlu
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 31st December 2017 - new year eve :)
#----------------------------------------------

import cv2
import color_histogram_feature_extraction
import knn_classifier
import os
import os.path
from PIL import Image
#cap = cv2.VideoCapture(0) #原来里面数值是1，结果运行不了，改成0后可以运行，可能是因为我用的是笔记本
imagePath = './test_picture/0038636.jpg'
#cap = cv2.imread(imagePath)

img1 = Image.open(imagePath)


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
    img2.save("./test_picture/linshi.jpg")
"""
def recognition():
    cut_lower_half(img1)
    cap = cv2.imread("./test_picture/linshi.jpg")
    frame = cap
    prediction = "n.a."
    color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    prediction = knn_classifier.main("training.data", "test.data")
"""    
cut_lower_half(img1)



frame = cv2.imread("./test_picture/linshi.jpg")
#ret, frame = cap.read()
#frame = cap
prediction = "n.a."

color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    
prediction = knn_classifier.main("training.data", "test.data")




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


