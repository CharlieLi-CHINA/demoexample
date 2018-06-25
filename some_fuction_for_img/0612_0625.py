# -*- coding: utf-8 -*-
import numpy as np #1
#import argparse #2
import imutils #3
from math import *
from PIL import Image
import cv2 #4
import os,sys
import numpy as np
from matplotlib import pyplot as plt
#path = "6.jpg"
abspath = "/home/charlie/Desktop/liqilv_bigdata_engineer_py3/test/"

def picture_rotate(path):

    image = cv2.imread(path)
    cv2.imshow("original",image)

    height,width = image.shape[:2]
    center = (width // 2, height // 2)
    degree = -4.5  # 旋转角度,负数表示顺时针,正数表示逆时针
    # 旋转后的尺寸
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
    #center = (0,0)

    M = cv2.getRotationMatrix2D(center,degree,1.0)
    M[0, 2] += (widthNew - width) / 2  # 重点在这步，目前不懂为什么加这步
    M[1, 2] += (heightNew - height) / 2  # 重点在这步

    rotated = cv2.warpAffine(image,M,(widthNew,heightNew),borderValue=(255,255,255))

    cv2.imshow('Rotated by' + ' ' + str(degree) +' ' + 'degrees',rotated)
    cv2.imwrite("rotated.jpg",rotated)

    cv2.waitKey(0)

def set_rotate_jiaodu(path):
    print('hh')
    image = cv2.imread(path)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY", gray)
    ret, thresh1 = cv2.threshold(gray, 250, 0, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 闭操作/开操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 3))
    closed = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
    # 膨胀和腐蚀操作的核函数
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 7))
    # 膨胀一次，让轮廓突出
    dilation = cv2.dilate(opened, element2, iterations=1)
    # 腐蚀一次，去掉细节
    erosion = cv2.erode(dilation, element1, iterations=1)
    # 再次膨胀，让轮廓明显一些
    dilation2 = cv2.dilate(erosion, element2, iterations=3)
    cv2.imshow("erzhihua", thresh1)
    cv2.imshow('bi', closed)
    cv2.imshow('kai', opened)
    cv2.imshow('dilation2', dilation2)
    cv2.waitKey(0)

def getAllImages(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    imageList = os.listdir(folder)
    imageList = [os.path.abspath(item) for item in imageList if os.path.isfile(os.path.join(folder, item))]
    return imageList
    
def idcard():
    result = ['张晓生', '大r', '多名', '铁驯', '民旗汉', '出生-7994:::10443,', '任地广东省汕头市湖阳区和平', '镇临昆上昆昌三直巷28号', '107=', '公民身份号码', '4405827994410045995']
    result_fine = []
    for i in range(0,len(result)):
        if len(result[i]) > 15 :
            idmb = result[i]
    result_fine.append(result[0])
    result_fine.append(idmb)
    #print(result_fine)
    return result_fine

def idcard_zhengfan_dange_paduan(img0):
    """
        思路：
        判断这张图是否是身份证正反面或者只有一面但是只是旋转了90度而已；
        通过计算其每一行的灰度值总和（存入数组sum），然后在做两次均值滤波--
        第一次滤波：sum数组元素比均值大，则减去均值，结果存入新数组sum_01，否则就为0
        第二次滤波：以sum_01为本，操作如第一次，得到新数组sum_01_2；
        然后统计sum_01_2数组中值为0的元素的坐标（也是img的纵坐标）、连续为0的值的长度；
        最后根据这个长度大小、坐标位置，判断是否是正反身份证或者旋转90度的身份证
        input----img
        output----roted_para,如果是0表示正反身份证照片，如果是1表示是旋转了90度的了身份证图
    """
    img = img0.copy()
    hight, width = img.shape[:2]
    # print("hight, width",hight, width)
    img = cv2.resize(img, (500, int(hight * 1. / width * 500)), cv2.INTER_AREA)  # 重新调整图片大小
    hight_new, width_new = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sum_x = []
    sum_y = []
    for i in range(0, hight_new):  # 行统计，统计每一行的像素灰度值总数
        sumx = np.sum(gray[i, :])
        sum_x.append(sumx)

    for j in range(0, width_new):  # 列统计，统计每一列的像素灰度值总数
        sumy = np.sum(gray[:, j])
        sum_y.append(sumy)

    sum_x_mean = np.mean(sum_x)
    sum_y_mean = np.mean(sum_y)
    sum_x_01 = []
    sum_y_01 = []
    for k in range(0, len(sum_x)):#第一次滤波
        if sum_x[k] >= sum_x_mean:
            sum_x_01.append(sum_x[k] - sum_x_mean)
            # sum_x_01.append(1)
        else:
            sum_x_01.append(0)

    for g in range(0, len(sum_y)):
        if sum_y[g] >= sum_y_mean:
            sum_y_01.append(sum_y[g] - sum_y_mean)
            # sum_y_01.append(1)
        else:
            sum_y_01.append(0)

    sum_x_mean_2 = np.mean(sum_x_01)
    sum_y_mean_2 = np.mean(sum_y_01)
    sum_x_01_2 = []
    sum_y_01_2 = []
    for k in range(0, len(sum_x_01)):#第二次滤波
        if sum_x_01[k] >= sum_x_mean_2:
            sum_x_01_2.append(sum_x_01[k] - sum_x_mean_2)
            # sum_x_01.append(1)
        else:
            sum_x_01_2.append(0)

    for g in range(0, len(sum_y_01)):
        if sum_y_01[g] >= sum_y_mean_2:
            sum_y_01_2.append(sum_y_01[g] - sum_y_mean_2)
            # sum_y_01.append(1)
        else:
            sum_y_01_2.append(0)


    #统计数组中值为0的元素的坐标（也是img的纵坐标）、连续为0的值的长度
    zeros_nmupy, zeros_begin, zeros_finis = 0, 0, 0
    zeros_ticks_begin = []
    zeros_ticks_finish = []
    for i in range(len(sum_x_01_2) - 1):
        if sum_x_01_2[i] == 0 and sum_x_01_2[i - 1] != 0 and sum_x_01_2[i + 1] == 0 and i > 1:  # 遇到元素为0，下一个元素也为0，则开始计算
            zeros_nmupy += 1
            # zeros_begin = i
            continue
        if sum_x_01_2[i] != 0 and sum_x_01_2[i - 1] == 0 and i > 1:  # 遇到元素不为0，前一个元素为0，则结束计算
            zeros_begin = i - zeros_nmupy
            zeros_nmupy = 0
            zeros_finish = i
            # if (zeros_finish - zeros_begin) >= (len(sum_x_01_2) / 3 ):
            zeros_ticks_begin.append(zeros_begin)
            zeros_ticks_finish.append(zeros_finish)
            continue
    print("zeros_ticks  begin,finish", zeros_ticks_begin, zeros_ticks_finish)
    lenth = 0
    leng = []
    for i in range(len(zeros_ticks_begin)):
        if len(zeros_ticks_begin) == len(zeros_ticks_begin):
            lenth = zeros_ticks_finish[i] - zeros_ticks_begin[i]
            if lenth > len(sum_x_01_2) // 10:
                leng.append(lenth)
                continue
    # zeros_nmupy = 0
    # zeros_ticks_begin = []
    # zeros_ticks_finish = []
    # for i in range(len(sum_x_01_2)-1):
    #     if sum_x_01_2[i] == 0 and sum_x_01_2[i-1] != 0  and sum_x_01_2[i+1] == 0 and i >1 :#遇到元素为0，下一个元素也为0，则开始计算
    #         zeros_nmupy += 1
    #         # zeros_begin = i
    #         continue
    #     if sum_x_01_2[i] != 0 and sum_x_01_2[i-1] == 0 and i >1:#遇到元素不为0，前一个元素为0，则结束计算
    #         zeros_begin = i - zeros_nmupy
    #         zeros_nmupy = 0
    #         zeros_finish = i
    #         # if (zeros_finish - zeros_begin) >= (len(sum_x_01_2) / 3 ):
    #         zeros_ticks_begin.append(zeros_begin)
    #         zeros_ticks_finish.append(zeros_finish)
    #         continue
    # print("zeros_ticks  begin,finish",zeros_ticks_begin,zeros_ticks_finish)
    # lenth = 0
    # leng = []
    # for i in range(0,len(zeros_ticks_begin)):
    #     lenth = zeros_ticks_finish[i] - zeros_ticks_begin[i]
    #     if lenth > (len(sum_x_01_2) / 10):
    #         leng.append(lenth)
    #     # if len(zeros_ticks_begin) == len(zeros_ticks_begin):
    #     #     lenth = zeros_ticks_finish[i] - zeros_ticks_begin[i]
    #     #     if lenth > (len(sum_x_01_2) / 10):
    #     #         leng.append(lenth)
    #     #         # continue

    # 统计数组中值为0的元素的坐标（也是img的横坐标）、连续为0的值的长度
    zeros_nmupy_x, zeros_begin_x, zeros_finis_x = 0, 0, 0
    zeros_ticks_begin_x = []
    zeros_ticks_finish_x = []

    for i in range(0, (len(sum_y_01_2))):
        if sum_y_01_2[i] == 0:  # 遇到元素为0，下一个元素也为0，则开始计算
            zeros_nmupy_x = zeros_nmupy_x + 1
        if (sum_y_01_2[i] > 0) or (i == len(sum_y_01_2) - 1):  # 遇到元素不为0，前一个元素为0，则结束计算
            if sum_y_01_2[0] == 0:
                break
            if (zeros_nmupy_x > 0):
                zeros_begin_x = i - zeros_nmupy_x
                # print("zeros_begin_x", zeros_begin_x)
                zeros_nmupy_x = 0
                zeros_finish_x = i
                # if (zeros_finish - zeros_begin) >= (len(sum_x_01_2) / 3 ):
                zeros_ticks_begin_x.append(zeros_begin_x)
                zeros_ticks_finish_x.append(zeros_finish_x)
                continue

    print("zeros_ticks  begin_x,finish_x", zeros_ticks_begin_x, zeros_ticks_finish_x)

    lenth_x = 0
    leng_x = []
    for i in range(0, len(zeros_ticks_begin_x)):
        lenth_x = zeros_ticks_finish_x[i] - zeros_ticks_begin_x[i]
        # print("lenth_x", lenth_x)
        # leng_x.append(lenth_x)
        if lenth_x > (len(sum_y_01_2) / 10):
            leng_x.append(lenth_x)

    degree = 0
    print("lenth", leng)
    print("leng_x", leng_x)
    bi = max(leng_x) if leng_x else 0
    for i in range(1, len(leng)):
        degree = 1 if bi > leng[i] else 0

    roted_para = 0 if degree == 1 else 1
    return roted_para




def hanglie_tongji(path):
    """
    思路：
    将图像缩放到固定大小，为了尽量减少计算复杂度，计算其每一行的灰度值，
    如果出现突变，那么可能就是身份证边缘，同时，也可以对列进行计算，
    这样就会大致知道行列突变的高度，
    就能确认其形状，进而确定是够要做旋转变换，或者是切割。
    考虑使用numpy数组进行切片计算这样会在计算复杂度上降低点。
    """
    img = cv2.imread(path)
    hight, width = img.shape[:2]
    print("img h w", hight, width)
    img = cv2.resize(img, (500, int(hight * 1. / width * 500)), cv2.INTER_AREA)  # 重新调整图片大小
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret,gray = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    # gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 2)
    hight_new, width_new = img.shape[:2]
    print("img h_new w_new", hight_new, width_new)
    cv2.imshow("oringin", img)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    sum_x = []
    sum_y = []
    sum_x_d = []
    sum_y_d = []
    for i in range(0,hight_new):#行统计，统计每一行的像素灰度值总数
        sumx = np.sum(gray[i,:])
        sum_x.append(sumx)
        # if i >0 and i < hight_new -11 :#类似于求导
        #     sumx_d = np.sum(gray[i+10,:]) - np.sum(gray[i,:])
        #     sum_x_d.append(sumx_d)

    for j in range(0,width_new):#列统计，统计每一列的像素灰度值总数
        sumy = np.sum(gray[:,j])
        sum_y.append(sumy)
        # if j >0 and j < width_new-11 :#类似于求导
        #     sumy_d = np.sum(gray[:,j+10]) - np.sum(gray[:,j])
        #     sum_y_d.append(sumy_d)
    sum_x_mean = np.mean(sum_x)
    sum_y_mean = np.mean(sum_y)
    sum_x_01 = []
    sum_y_01 = []
    for k in range(0,len(sum_x)):
        if sum_x[k] >= sum_x_mean:
            sum_x_01.append(sum_x[k] - sum_x_mean )
            # sum_x_01.append(1)
        else:
            sum_x_01.append(0)

    for g in range(0,len(sum_y)):
        if sum_y[g] >= sum_y_mean:
            sum_y_01.append(sum_y[g] - sum_y_mean )
            # sum_y_01.append(1)
        else:
            sum_y_01.append(0)
    # sum_x_gd = []
    # sum_y_gd = []
    # sum_x_gd = np.argsort(sum_x)
    # sum_y_gd = np.argsort(sum_y)
    # sum_x_zhong = sum_x_gd[len(sum_x_gd)//2]
    # sum_y_zhong = sum_y_gd[len(sum_y_gd)//2]
    print("x sum junzhi,y sum junzhi",np.mean(sum_x),np.mean(sum_y))

    # print("sum x zhongzhi and sum y zhongzhi ",sum_x_zhong,sum_y_zhong)

    # sum_x_01_z = []
    # sum_y_01_z = []
    # for h in range(0, len(sum_x)):
    #     if sum_x[h] >= sum_x_zhong:
    #         # sum_x_01.append(sum_x[k] - sum_x_mean)
    #         sum_x_01_z.append(1)
    #     else:
    #         sum_x_01_z.append(0)
    #
    # for j in range(0, len(sum_y)):
    #     if sum_y[j] >= sum_y_zhong:
    #         # sum_y_01.append(sum_y[g] - sum_y_mean)
    #         sum_y_01_z.append(1)
    #     else:
    #         sum_y_01_z.append(0)
    sum_x_mean_2 = np.mean(sum_x_01)
    sum_y_mean_2 = np.mean(sum_y_01)
    sum_x_01_2 = []
    sum_y_01_2 = []
    for k in range(0, len(sum_x_01)):
        if sum_x_01[k] >= sum_x_mean_2:
            sum_x_01_2.append(sum_x_01[k] - sum_x_mean_2)
            # sum_x_01.append(1)
        else:
            sum_x_01_2.append(0)

    for g in range(0, len(sum_y_01)):
        if (sum_y_01[g]) >= (sum_y_mean_2 ):
            sum_y_01_2.append(sum_y_01[g] - sum_y_mean_2)
            # sum_y_01.append(1)
        else:
            sum_y_01_2.append(0)
    print("sum_x_01 junzhi,sum_y_01 junzhi,sum_x_01_2 junzhi,sum_y_01_2 junzhi", np.mean(sum_x_01), np.mean(sum_y_01),
          np.mean(sum_x_01_2), np.mean(sum_y_01_2))


    plt.figure(1)
    plt.subplot(2, 1,1),plt.plot(sum_x),plt.title("x sum")
    plt.subplot(2, 1, 2), plt.plot(sum_y),plt.title("y sum")
    # plt.subplot(2, 2, 3), plt.plot(sum_x_d), plt.title("x sum _d")
    # plt.subplot(2, 2, 4), plt.plot(sum_y_d), plt.title("y sum _d")

    plt.figure(2)
    plt.subplot(2, 1, 1), plt.plot(sum_x_01), plt.title("sum_x_01")
    plt.subplot(2, 1, 2), plt.plot(sum_y_01), plt.title("sum_y_01")

    plt.figure(3)
    plt.subplot(2, 1, 1), plt.plot(sum_x_01_2), plt.title("sum_x_01_2")
    plt.subplot(2, 1, 2), plt.plot(sum_y_01_2), plt.title("sum_y_01_2")

    plt.show()

    # 统计数组中值为0的元素的坐标（也是img的纵坐标）、连续为0的值的长度
    zeros_nmupy,zeros_begin, zeros_finis= 0,0,0
    zeros_ticks_begin = []
    zeros_ticks_finish = []
    for i in range(0,len(sum_x_01_2)):
        if sum_x_01_2[i] == 0 :  # 遇到元素为0,则开始计算
            zeros_nmupy = zeros_nmupy + 1
            # zeros_begin = i
            # continue
        if sum_x_01_2[i] != 0 and sum_x_01_2[i - 1] == 0 and i > 1:  # 遇到元素不为0，前一个元素为0，则结束计算
            zeros_begin = i - zeros_nmupy
            zeros_nmupy = 0
            zeros_finish = i
            # if (zeros_finish - zeros_begin) >= (len(sum_x_01_2) / 3 ):
            zeros_ticks_begin.append(zeros_begin)
            zeros_ticks_finish.append(zeros_finish)
            continue
    print("zeros_ticks  begin,finish", zeros_ticks_begin, zeros_ticks_finish)
    lenth = 0
    leng = []
    for i in range(len(zeros_ticks_begin)):
        if len(zeros_ticks_begin) == len(zeros_ticks_begin):
            lenth = zeros_ticks_finish[i] - zeros_ticks_begin[i]
            if lenth > len(sum_x_01_2)//10:
                leng.append(lenth)
                continue

    # 统计数组中值为0的元素的坐标（也是img的横坐标）、连续为0的值的长度
    zeros_nmupy_x, zeros_begin_x, zeros_finis_x = 0, 0, 0
    zeros_ticks_begin_x = []
    zeros_ticks_finish_x = []

    for i in range(0, (len(sum_y_01_2))):
        if sum_y_01_2[i] == 0:  # 遇到元素为0，下一个元素也为0，则开始计算
            zeros_nmupy_x = zeros_nmupy_x + 1
            # print("zeros_nmupy_x",zeros_nmupy_x)
            # zeros_begin_x = i
            # continue

        if (sum_y_01_2[i] > 0) or (i == len(sum_y_01_2) - 1):  # 遇到元素不为0，前一个元素为0，则结束计算
            if sum_y_01_2[0] == 0:
                break
            if (zeros_nmupy_x > 0):
                zeros_begin_x = i - zeros_nmupy_x
                # print("zeros_begin_x", zeros_begin_x)
                zeros_nmupy_x = 0
                zeros_finish_x = i
                # if (zeros_finish - zeros_begin) >= (len(sum_x_01_2) / 3 ):
                zeros_ticks_begin_x.append(zeros_begin_x)
                zeros_ticks_finish_x.append(zeros_finish_x)
                continue

                # else:
                #     continue
    print("zeros_ticks  begin_x,finish_x", zeros_ticks_begin_x, zeros_ticks_finish_x)

    lenth_x = 0
    leng_x = []
    for i in range(0, len(zeros_ticks_begin_x)):
        lenth_x = zeros_ticks_finish_x[i] - zeros_ticks_begin_x[i]
        # print("lenth_x", lenth_x)
        # leng_x.append(lenth_x)
        if lenth_x > (len(sum_y_01_2) / 10):
             leng_x.append(lenth_x)

        # if len(zeros_ticks_begin_x) == len(zeros_ticks_finish_x):
        #     lenth_x = zeros_ticks_finish_x[i] - zeros_ticks_begin_x[i]
        #     if lenth_x > (len(sum_y_01_2) / 10):
        #         print("lenth_x", lenth_x)
        #         leng_x.append(lenth_x)
        # continue

    degree = 0
    print("lenth",leng)
    print("leng_x",leng_x)
    bi = max(leng_x) if leng_x else 0
    print("bi",bi)
    for i in range(1,len(leng)):
        # degree = 1  if bi > leng[i] else 0

        if bi > leng[i] :
            degree = 1
        else:
            degree = 0
    if degree == 1:
        return 0
    else:
        return 1
    # return 0 if degree == 1 else 1





def idcard_find_binayuan(path):
    #看灰度图、hsv图、hsv各个通道显示图、hsv的0通道直方图、对hsv的0通道进行二值化并取反、开闭运算、寻找轮廓、画出轮廓，以上均为分析
    #20180622 失败了，没有找到什么好的东西，或者特征出来
    img = cv2.imread(path)
    hight, width = img.shape[:2]
    print("img h w",hight, width)
    img = cv2.resize(img, (500, int(hight * 1. / width * 500)), cv2.INTER_AREA)  # 重新调整图片大小
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#色调（H），饱和度（S），明度（V）
    print("hsv shape",hsv.shape)
    cv2.imshow("GRAY", gray)
    cv2.imshow("HSV", hsv)
    cv2.imshow("HSV 0", hsv[:,:,0])
    cv2.imshow("HSV 1", hsv[:, :, 1])
    cv2.imshow("HSV 2", hsv[:, :, 2])
    # cv2.waitKey(0)
    hsv_0 = hsv[:,:,0].copy()
    # thresh_hsv_0 = cv2.adaptiveThreshold(hsv_0, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)
    ret, thresh_hsv_0 = cv2.threshold(hsv_0, 0, 255, cv2.THRESH_BINARY_INV)  # 二值化
    ret2, thresh2_hsv_0 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)  # 二值化
    # 闭操作/开操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    # thresh_hsv_0 = cv2.morphologyEx(thresh_hsv_0, cv2.MORPH_CLOSE, kernel)
    thresh_hsv_0 = cv2.morphologyEx(thresh_hsv_0, cv2.MORPH_OPEN, kernel)
    thresh_hsv_0 = cv2.morphologyEx(thresh_hsv_0, cv2.MORPH_OPEN, kernel2)
    ret, thresh_hsv_0 = cv2.threshold(thresh_hsv_0, 0, 255, cv2.THRESH_BINARY_INV)  # 二值化
    cv2.imshow("thresh_hsv_0", thresh_hsv_0)
    cv2.imshow("thresh_hsv_0_erzhihua", thresh2_hsv_0)
    # 寻找轮廓
    thresh_hsv_0, contours, hierarchy = cv2.findContours(thresh_hsv_0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    box = []
    # 筛选面积小的
    for i in range(len(contours)):

        cnt = contours[i]
        # 计算该轮廓的面积
        area = cv2.contourArea(cnt)
        if cnt.shape[0] != 8:
            continue
        print('cnt',cnt,cnt.shape,"over",cnt.shape[0])
        box.append(cnt)



        # x, y, w, h = cv2.boundingRect(cnt)
        # x1 = x
        # y1 = y
        # x2 = x + w
        # y2 = y
        # x3 = x
        # y3 = y + h
        # x4 = x + w
        # y4 = y + h
        # # hight, width
        # if w > (width/3):
        #     box.append([x1, y1, x2, y2, x3, y3, x4, y4])  # 保存每一个符合条件的边框
        #     print(box)
        # 用绿线画出这些找到的轮廓
    # for box in contours:
    for i in range(len(box)):
        boxi= box[i]
        cv2.drawContours(img, [boxi], 0, (0, 255, 0), 2)
        cv2.imshow('thresh_hsv_0_lunkuo', img)
        # cv2.imwrite("img11.jpg", thresh_hsv
    cv2.waitKey(0)
    hsv_0_hist = cv2.calcHist([hsv], [0], None, [256], [0.0, 255.0])
    plt.plot(hsv_0_hist)
    plt.show()

def erzhihua(path):
    img = cv2.imread(path)
    hight, width = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY", gray)
    # ret, thresh1 = cv2.threshold(gray, 137, 255, cv2.THRESH_BINARY)
    thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
    # ret, thresh1 = cv2.threshold(thresh1, 127, 255, cv2.THRESH_BINARY_INV)  # 二值化，黑色变白，白色变黑

    thresh1 = cv2.resize(thresh1, (1000, int(hight * 1. / width * 1000)), cv2.INTER_AREA)  # 重新调整图片大小
    img00 = cv2.resize(img, (1000, int(hight * 1. / width * 1000)), cv2.INTER_AREA)  # 重新调整图片大小
    # 闭操作/开操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)

    # # 膨胀和腐蚀操作的核函数
    # element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    # element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 7))
    # # 膨胀一次，让轮廓突出
    # thresh1 = cv2.dilate(thresh1, element2, iterations=1)
    # # 腐蚀一次，去掉细节
    # thresh1 = cv2.erode(thresh1, element1, iterations=1)
    # # 再次膨胀，让轮廓明显一些
    # thresh1 = cv2.dilate(thresh1, element2, iterations=1)

    # 寻找轮廓
    img11,contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    box = []
    # 筛选面积小的
    for i in range(len(contours)):

        cnt = contours[i]
        # 计算该轮廓的面积
        area = cv2.contourArea(cnt)

        # 面积小的都筛选掉
        if (area < 8000):
            continue
        #
        # # 轮廓近似，作用很小
        # epsilon = 0.001 * cv2.arcLength(cnt, True)
        # approx = cv2.approxPolyDP(cnt, epsilon, True)

        # 找到最小的矩形，该矩形可能有方向
        # cv2.minAreaRect返回一个 Box2D 结构--矩形左上角角点的坐标、高宽、旋转角度
        # rect = cv2.minAreaRect(cnt)
        # print "rect is(疑似车牌的轮廓矩形的左上角角点的坐标、高宽、旋转角度): "
        # print rect
        # print "liqilv"

        # x, y, w, h
        x, y, w, h = cv2.boundingRect(cnt)
        x1 = x
        y1=y
        x2=x+w
        y2=y
        x3=x
        y3=y+h
        x4=x+w
        y4=y+h
        if h > 100 and w > 100 and x >1 and y >1:  # 设定条件 w > 1.4 * h and w < 1.8 * h and
            # cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 10)
            box.append([x1, y1, x2, y2,x3, y3,x4, y4])  # 保存每一个符合条件的边框
        print(box)

    # 用绿线画出这些找到的轮廓
    for box in contours:
        cv2.drawContours(img00, [box], 0, (0, 255, 0), 2)
        cv2.imshow('img11', img00)
        cv2.imwrite("img11.jpg",img00)

    cv2.imshow("erzhihua-50", thresh1)
    cv2.imwrite("erzhihua-0.jpg",thresh1)
    cv2.waitKey(0)

    # im_gray = gray.copy()
    # im_at_mean = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
    # plt.axis("off")
    # plt.title("Adaptive Thresholding with mean weighted average")
    # cv2.imshow(im_at_mean, cmap='gray')
    # plt.show()
    # cv2.imwrite("im_at_mean.jpg",im_at_mean)
    # cv2.waitKey(0)

    # #二值化加投影
    # img = cv2.imread(path, 0)
    # img = cv2.medianBlur(img, 5)
    # ret, th1 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    # th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 2)
    # th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 2)
    #
    # titles = ['orgianl Image', 'Gllobal Thresholding(v=127)', 'ADaptive Mean Thresholding',
    #           'Adaptive Gaussian Thresholding']
    # images = [img, th1, th2, th3]
    #
    # for i in range(4):
    #     # 闭操作/开操作
    #     grayimg = images[i]
    #     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
    #     closed = cv2.morphologyEx(grayimg, cv2.MORPH_CLOSE, kernel)
    #     opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
    #     # # 膨胀和腐蚀操作的核函数
    #     # element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    #     # element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 7))
    #     # # 膨胀一次，让轮廓突出
    #     # dilation = cv2.dilate(opened, element2, iterations=1)
    #     # # 腐蚀一次，去掉细节
    #     # erosion = cv2.erode(dilation, element1, iterations=1)
    #     # # 再次膨胀，让轮廓明显一些
    #     # dilation2 = cv2.dilate(erosion, element2, iterations=3)
    #     images[i] = opened
    # img_nupm = images[3].copy()
    # thresh11 = images[3].copy()
    #
    # (h, w) = thresh11.shape  # 返回高和宽
    # # print(h,w)#s输出高和宽
    # # a = np.zeros(w)
    # a = [0 for z in range(0, h)]
    # # print(a)  # a = [0,0,0,0,0,0,0,0,0,0,...,0,0]初始化一个长度为h的数组，用于记录每一hang的黑点个数
    #
    # # 记录每一行的波峰
    # for i in range(0, h):  # 遍历一hang
    #     for j in range(0, w):  # 遍历一lie
    #         if thresh11[i, j] == 0:  # 如果此点为黑点
    #             a[i] += 1  # 该hang的计数器加一计数
    #             thresh11[i, j] = 255  # 记录完后将其变为白色
    #     # print (j)
    #
    # #
    # for i in range(0, h):  # 遍历每一hang
    #     for j in range((w - a[i]), w):  # 从该hang应该变黑的最顶部的点开始向最底部涂黑
    #         thresh11[i, j] = 0  # 涂黑
    #
    # #print(thresh11)
    # plt.imshow(thresh11, cmap=plt.gray())
    # # plt.title("touying")
    # # plt.xticks([]), plt.yticks([])
    # plt.show()
    # # 此时的thresh1便是一张图像向垂直方向上投影的直方图
    #
    #
    # #
    # for i in range(4):
    #     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    #
    #     plt.title(titles[i])
    #     plt.xticks([]), plt.yticks([])
    #
    # # plt.subplot(2, 3, 5)
    #
    # plt.show()


def delete_blue_piexl(path):
    i = 1
    j = 1
    img = Image.open(path)  # 读取系统的内照片
    # img = np.array(img)
    # print(img.size)  # 打印图片大小
    # print(img.getpixel((4, 4)))
    width = img.size[0]  # 长度
    height = img.size[1]  # 宽度

    # height, width = img.shape[:2]
    for i in range(0, width):  # 遍历所有长度的点
        for j in range(0, height):  # 遍历所有宽度的点
            data = (img.getpixel((i, j)))  # 打印该图片的所有点
            # print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            # print(data[0])  # 打印RGBA的r值
            # if (data[0] >= 170 and data[1] >= 170 and data[2] >= 170):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
            #     img.putpixel((i, j), (234, 53, 57, 255))  # 则这些像素点的颜色改成大红色

            if (data[1] >= 170 and data[2] >= 200):  # g值大于190,并且b值大于235
                img.putpixel((i, j), (255, 255, 255, 255))  # 则这些像素点的颜色改成
    img = img.convert("RGB")  # 把图片强制转成RGB
    img.save("testee1.jpg")  # 保存修改像素点后的图片

def shibie_blue():
    cap = cv2.VideoCapture(0)

    # set blue thresh
    lower_blue = np.array([78, 43, 46])
    upper_blue = np.array([110, 255, 255])

    while (1):
        # get a frame and show
        ret, frame = cap.read()
        cv2.imshow('Capture', frame)

        # change to hsv model
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # get mask
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        cv2.imshow('Mask', mask)

        # detect blue
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('Result', res)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def blue(path):
    #将身份证上面的蓝色字体去掉，以免影响识别效果
    frame = cv2.imread(path)
    # 高斯模糊
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # set blue thresh
    lower_blue = np.array([78, 43, 46])
    upper_blue = np.array([110, 255, 255])
    cv2.imshow('Capture', frame)

    # change to hsv model
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get mask
    mask0 = cv2.inRange(hsv, lower_blue, upper_blue)

    ret, mask = cv2.threshold(mask0, 127, 255, cv2.THRESH_BINARY_INV)#二值化，黑色变白，白色变黑
    # 闭操作/开操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
    # opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Mask', mask)
    cv2.imwrite("Mask.jpg", mask)
    cv2.imshow('open-close', opened)
    cv2.imwrite("open-close.jpg", opened)
    # 膨胀和腐蚀操作的核函数
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 膨胀一次，让轮廓突出
    dilation = cv2.dilate(closed, element2, iterations=1)
    # 腐蚀一次，去掉细节
    erosion = cv2.erode(dilation, element1, iterations=1)
    # 再次膨胀，让轮廓明显一些
    dilation2 = cv2.dilate(erosion, element2, iterations=3)
    cv2.imshow('dilation2', dilation2)
    cv2.imwrite("dilation2.jpg", dilation2)

    # 别忘了是三通道图像，因此这里使用 merge 变成 3 通道
    thresh1 = cv2.merge((dilation2, dilation2, dilation2))
    # 按位操作
    res1 = cv2.bitwise_and(frame, thresh1)
    # res1 = np.hstack((frame, thresh1, res1))
    cv2.imwrite('res1.jpg', res1)
    # 显示图像
    cv2.imshow('1', res1)
    # contours, hierarchy = cv2.findContours(mask0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow("lunkuo",contours)


    # detect blue
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Result', res)
    cv2.imwrite("res.jpg",res)

    # while (1):
    #     # get a frame and show
    #     # ret, frame = cap.read()
    #     cv2.imshow('Capture', frame)
    #
    #     # change to hsv model
    #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #
    #     # get mask
    #     mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #     cv2.imshow('Mask', mask)
    #
    #     # detect blue
    #     res = cv2.bitwise_and(frame, frame, mask=mask)
    #     cv2.imshow('Result', res)
    #
    #     # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     #     break


    # cap.release()
    # cv2.destroyAllWindows()
    cv2.waitKey(0)

def touying(path):
    img = cv2.imread(path)  # 读取图片，装换为可运算的数组
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将BGR图转为灰度图
    ret, thresh1 = cv2.threshold(GrayImage, 80, 255, cv2.THRESH_BINARY)  # 将图片进行二值化（130,255）之间的点均变为255（背景）
    # print(thresh1[0,0])#250  输出[0,0]这个点的像素值               #返回值ret为阈值
    # print(ret)#130
    (h, w) = thresh1.shape  # 返回高和宽
    # print(h,w)#s输出高和宽
    # a = np.zeros(w)
    a = [0 for z in range(0, w)]
    # print(a)  # a = [0,0,0,0,0,0,0,0,0,0,...,0,0]初始化一个长度为w的数组，用于记录每一列的黑点个数

    # 记录每一列的波峰
    for j in range(0, w):  # 遍历一列
        for i in range(0, h):  # 遍历一行
            if thresh1[i, j] == 0:  # 如果改点为黑点
                a[j] += 1  # 该列的计数器加一计数
                thresh1[i, j] = 255  # 记录完后将其变为白色
        # print (j)

    #
    for j in range(0, w):  # 遍历每一列
        for i in range((h - a[j]), h):  # 从该列应该变黑的最顶部的点开始向最底部涂黑
            thresh1[i, j] = 0  # 涂黑

    # 此时的thresh1便是一张图像向垂直方向上投影的直方图
    # 如果要分割字符的话，其实并不需要把这张图给画出来，只需要的到a=[]即可得到想要的信息



    # number_zero = 0
    # for i in range(0,len(a)):
    #     if a[i] == 0:
    #         number_zero += 1
    #     number_zeros = number_zero
    #     if number_zeros > 15 and a[i+1] > 0:
    #         number_zeros_x_anction = i
    #         break
    #
    # for i in range(len(a)-1,-1,-1):
    #     if a[i] ==0:
    #         number_zero += 1
    #     number_zeros = number_zero
    #     if number_zeros > 5 and a[i-1] > 0:
    #         number_zero_x_end = i
    #         break
    # print("zero a",number_zeros_x_anction,number_zero_x_end)

    # img2 =Image.open('0002.jpg')
    # img2.convert('L')
    # img_1 = np.array(img2)

    #
    # plt.imshow(thresh1, cmap=plt.gray())
    # plt.show()
    # cv2.imshow('img', thresh1)
    # cv2.imwrite('thresh1.jpg',thresh1)
    # print(a)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return thresh1



def get_words_space(path):
    #获取图片非空白区域，即包含文字信息的横坐标，即前后的横坐标
    img = cv2.imread(path)  # 读取图片，装换为可运算的数组
    # img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将BGR图转为灰度图
    ret, thresh1 = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)  # 将图片进行二值化（130,255）之间的点均变为255（背景）
    (h, w) = thresh1.shape  # 返回高和宽
    a = [0 for z in range(0, w)]
    # print(a)  # a = [0,0,0,0,0,0,0,0,0,0,...,0,0]初始化一个长度为w的数组，用于记录每一列的黑点个数
    # 记录每一列的波峰
    for j in range(0, w):  # 遍历一列
        for i in range(0, h):  # 遍历一行
            if thresh1[i, j] == 0:  # 如果改点为黑点
                a[j] += 1  # 该列的计数器加一计数
                thresh1[i, j] = 255  # 记录完后将其变为白色
        # print (j)
    #
    for j in range(0, w):  # 遍历每一列
        for i in range((h - a[j]), h):  # 从该列应该变黑的最顶部的点开始向最底部涂黑
            thresh1[i, j] = 0  # 涂黑
    # 此时的thresh1便是一张图像向垂直方向上投影的直方图
    # 如果要分割字符的话，其实并不需要把这张图给画出来，只需要的到a=[]即可得到想要的信息

    #计算连续的文字区域，number_zeros_x_anction,number_zero_x_end为横坐标
    number_zero = 0
    number_zeros_x_anction = 0
    number_zero_x_end = 0
    number_zeros =0
    for i in range(0,len(a)):
        if a[i] == 0:
            number_zero += 1
        number_zeros = number_zero
        if number_zeros >= 15 and a[i+1] > 0:
            number_zeros_x_anction = i
            break

    for i in range(len(a)-1,-1,-1):
        if a[i] == 0:
            number_zero += 1
        number_zeros = number_zero
        if number_zeros > 5 and a[i-1] > 0:
            number_zero_x_end = i
            break
    # print("zero a",number_zeros_x_anction,number_zero_x_end)
    return (number_zeros_x_anction,number_zero_x_end)

def delete_none_words_zone(path):
    for i in os.listdir(path):
        x1 = 0
        x2 = 0

        path_file = os.path.join(path,i)
        x1, x2 = get_words_space(path_file)
        # img = cv2.imread(path_file)
        # cv2.imshow("img for only words",img)
        img = Image.open(path_file)
        x, y = img.size
        if x1 > 15 and x2 >15:
            box = [x1, 0, x2, y]
            img2 = img.crop(box)
            img2.save(path_file)
        else:
            break



def  del_file(path): #删除文件夹下的原有文件
    path_files = []
    for i in os.listdir(path):
        path_file = os.path.join(path,i)
        print(path_file)
        path_files.append(path_file)
    return path_files

# def mathc_img(image,Target,value):

def mathc_img(path,path_muban):
    #模板匹配
    # import cv2
    # import numpy as np
    # img_rgb = cv2.imread(image)
    # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # template = cv2.imread(Target,0)
    # w, h = template.shape[::-1]
    # res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    # threshold = value
    # loc = np.where( res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
    # cv2.imshow('Detected',img_rgb)
    # cv2.imwrite('mubanpip.jpg',img_rgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img = cv2.imread(path, 0)
    img_origin = cv2.imread(path)
    # img2 = img.copy()
    template = cv2.imread(path_muban, 0)
    w, h = template.shape[::-1]

    # # 6 中匹配效果对比算法
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    # img = img2.copy()

    # method = eval(meth)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #     top_left = min_loc
    # else:
    #     top_left = max_loc
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print("top_left and w h", top_left, w, h)

    img_origin_h, img_origin_w = img_origin.shape[:2]
    print("img_origin_h,img_origin_w=", img_origin_h, img_origin_w)
    # cv2.rectangle(img, top_left, bottom_right, 255, 2)
    cv2.imwrite("caijian.jpg", img_origin[1:img_origin_h - 1, top_left[0] + w: img_origin_w, :])

    #
    # for meth in methods:
    #     img = img2.copy()
    #
    #     method = eval(meth)
    #
    #     res = cv2.matchTemplate(img, template, method)
    #     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #
    #     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #         top_left = min_loc
    #     else:
    #         top_left = max_loc
    #     bottom_right = (top_left[0] + w, top_left[1] + h)
    #     print("top_left and w h",top_left,w,h)
    #
    #     img_origin_h,img_origin_w = img_origin.shape[:2]
    #     print("img_origin_h,img_origin_w=",img_origin_h,img_origin_w)
    #     # cv2.rectangle(img, top_left, bottom_right, 255, 2)
    #     cv2.imwrite("caijian.jpg",img_origin[1:img_origin_h - 1, top_left[0] + w: img_origin_w, :])
    #
    #     print(meth)
    #     plt.subplot(221), plt.imshow(img2, cmap="gray")
    #     plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #     plt.subplot(222), plt.imshow(template, cmap="gray")
    #     plt.title('template Image'), plt.xticks([]), plt.yticks([])
    #     plt.subplot(223), plt.imshow(res, cmap="gray")
    #     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    #     plt.subplot(224), plt.imshow(img, cmap="gray")
    #     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    #     plt.show()


    # Read more: http://bluewhale.cc/2017-09-22/use-python-opencv-for-image-template-matching-match-template.html#ixzz5IvVJBCTb

if __name__ == '__main__':
    # path = sys.argv[1]
    path = "身份证3.jpg"
    # path = "333.png"
    # path = "身份证正反面.png"
    # img0 = cv2.imread(path)
    # roted_para = idcard_zhengfan_dange_paduan(img0)
    # print("roted_para",roted_para)
    # path = "25.jpg"
    # print(getAllImages(path))
    # erzhihua(abspath + "origin_picture/" + path)
    # idcard_find_binayuan(path)
    # delete_blue_piexl(path)
    # shibie_blue()
    # blue(path)
    # hanglie_tongji(path)
    print(hanglie_tongji(path))
    # imga = Image.open("./testpicture/"+str(0)+".jpg")
    # print(imga.shape)
    # touying(path)
    # x1,x2 = delete_none_words_space("./testpicture/"+str(0)+".jpg")
    # img2 = cv2.imread("./testpicture/"+str(0)+".jpg")
    # cv2.imwrite("./testpicture/"+str(0)+".jpg",img2[:, x1:x2, :])
    # print(delete_none_words_space(path))
    # print(x1,x2)

    # picture_rotate(path)
    # set_rotate_jiaodu(path)

    # path = del_file("./testpicture")
    # for i in range(0,len(path)):
    #     path_i = path[i]
    #     touyingtu0 = touying(path_i)
    #     # touyingtu = cv2.resize(touyingtu0, (371, 100), interpolation=cv2.INTER_CUBIC)
    #     # cv2.imshow("touyingtu"+str(i),touyingtu)
    #     # cv2.imwrite("touying"+str(i)+".jpg",touyingtu)
    #     # cv2.waitKey(0)
    #     # cv2.destroyAllWindows()
    #     plt.imshow(touyingtu0, cmap=plt.gray())
    #     plt.show()

    # image = ("0.jpg")
    # Target = ('sfz_xm.jpg')
    # value = 0.9
    # mathc_img(image, Target, value)
    # path = "身份证8.jpg"
    # path = "0.jpg"
    # path_muban = "sfz_xm.jpg"
    # mathc_img(path,path_muban)

    # path1= path[0]

    # delete_none_words_zone("./testpicture")

"""
#ap = argparse.ArgumentParser() #5
#ap.add_argument("-i", "--image", required=True,
       #         help="Path to the image") #6
#args = vars(ap.parse_args())  #7
path = "23.jpg"
image = cv2.imread(path) #8
cv2.imshow("原始图片", image) #9
(h,w) = image.shape[:2]
M = np.float32([[1, 0, 25], [0, 1, 50]]) #10
#M是平移矩阵,[1,0,x],其中x表示图像将向左或向右移动的距离,x是正值则向右移动，反之则左移。[0,1,y],其中y表示图像将向上或向下移动的距离，如果y是正值的话，则向下移动，如果是负值的话，则向上移动
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0])) #11 仿射变换，第二个参数是我们的平移矩阵，第三个希望展示的结果图片的大小，这里保持和原始图片一样大小
cv2.imshow("Shifted Down and Right", shifted) #12

M = np.float32([[1, 0, -50], [0, 1, -90]]) #13
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0])) #14
cv2.imshow("Shifted Up and Left", shifted) #15

shifted = imutils.translate(image, 0, 100) #16
cv2.imshow("Shifted down---", shifted) #17
cv2.waitKey(0) #18
"""
