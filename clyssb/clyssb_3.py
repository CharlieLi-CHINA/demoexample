# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:18:55 2017
fuction: 车辆颜色识别整个代码
update#20171215Fri.实现批量识别
@author: liqilv
"""
import sys,cv2,os,time
import numpy as np
from skimage import io

def preprocess(gray):
    # # 直方图均衡化
    # equ = cv2.equalizeHist(gray)
    # 高斯平滑    
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
    # 中值滤波
    median = cv2.medianBlur(gaussian, 5)
    # Sobel算子，X方向求梯度----参数 1,0 为只在 x 方向求一阶导数
    sobel = cv2.Sobel(median, cv2.CV_8U, 1, 0, ksize = 3)
    # 二值化，参数170是阈值，参数255是超过阈值的像素赋予255灰度值
    #返回值ret是图像的阈值，binary是二值化后的图像
    ret, binary = cv2.threshold(sobel, 170, 255, cv2.THRESH_BINARY)
    # 膨胀和腐蚀操作的核函数
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 7))
    # 膨胀一次，让轮廓突出
    dilation = cv2.dilate(binary, element2, iterations = 1)
    # 腐蚀一次，去掉细节
    erosion = cv2.erode(dilation, element1, iterations = 1)
    # 再次膨胀，让轮廓明显一些
    dilation2 = cv2.dilate(erosion, element2,iterations = 3)
    #cv2.imshow('dilation2',dilation2)
    #cv2.waitKey(0)，一个键盘绑定函数，当参数为0时要按下键盘才能使得程序继续运行
    #64 位系统中要将cv2.waitKey(0) 这行改成 cv2.waitKey(0)&0xFF
    #cv2.waitKey(0)&0xFF
    return dilation2
def findPlateNumberRegion(img):
    
    region = []
    # 查找轮廓
    # 第二个参数是轮廓检索模式，cv2.RETR_TREE意味着检测到完整的轮廓以及组织
    # 第三个参数是轮廓近似方法，cv2.CHAIN_APPROX_SIMPLE意味着最紧要描述轮廓的信息
    #返回值中，contours表示返回的轮廓，hierarchy表示轮廓的组织结构
    contours,hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 筛选面积小的
    for i in range(len(contours)):
        
        cnt = contours[i]
        # 计算该轮廓的面积
        area = cv2.contourArea(cnt)

        # 面积小的都筛选掉
        if (area < 2000):
            continue
        
        # 轮廓近似，作用很小
        epsilon = 0.001 * cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # 找到最小的矩形，该矩形可能有方向
        #cv2.minAreaRect返回一个 Box2D 结构--矩形左上角角点的坐标、高宽、旋转角度
        rect = cv2.minAreaRect(cnt)
        #print "rect is(疑似车牌的轮廓矩形的左上角角点的坐标、高宽、旋转角度): "
        #print rect
        #print "liqilv"

        # box是四个点的坐标
        box = cv2.cv.BoxPoints(rect)
        ##np.int0 可以用来省略小数点后面的数字（非四舍五入）
        box = np.int0(box)
        
        # 计算高和宽
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
       
        # 车牌正常情况下长高比在2.7-5之间
        ratio =float(width) / float(height)
        #print ratio
        if (ratio > 5 or ratio < 2):
            continue
        """---
        for i in range(4):
                print "box坐标"
                for j in range(1):
                    print box[i][0]
        print "height is"
        print height
        print "width is"
        print width
        ---"""
        region.append(box)
    return region

def detect(img):    
    # 用绿线画出这些找到的轮廓
    #drawContours函数中第二个参数是轮廓，第三个是轮廓的索引，接下来是颜色和厚度
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 形态学变换的预处理
    dilation = preprocess(gray)

    # 查找车牌区域
    region = findPlateNumberRegion(dilation)
    
    for box in region:
        cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
    """----------------------------------------------------
    
    #通过改变切割的车牌的纵、横坐标来确定车头盖区域纵坐标
    -------------------------------------------------------"""
    gaodu = abs(box[0, 1]-box[1, 1])
    kuandu = abs(box[0, 0]-box[2, 0])
    box[0][0] = box[0][0] - 0.5*kuandu
    box[1][0] = box[1][0] - 0.5*kuandu
    box[2][0] = box[2][0] + 0.5*kuandu
    box[3][0] = box[3][0] + 0.5*kuandu
    #print "gaodu,kuandu",gaodu,kuandu
    for i in range(4):
        #更改纵坐标
        box[i, 1] = box[i, 1] - 2.5*gaodu
        #box[i, 0] = 2*box[i, 0] 
        #print "new x,new y:",box[i, 0],box[i, 1]
    """---------------------------------------------------
    ------------------------------------------------------"""
    for box in region:
        cv2.drawContours(img, [box], 0, (255, 255, 255), 2)
    
    ys = [box[0, 1], box[1, 1], box[2, 1], box[3, 1]]
    xs = [box[0, 0], box[1, 0], box[2, 0], box[3, 0]]
    
    #print "xs,ys",xs,ys
    ys_sorted_index = np.argsort(ys)
    xs_sorted_index = np.argsort(xs)

    x1 = box[xs_sorted_index[0], 0]
    x2 = box[xs_sorted_index[3], 0]
    
    y1 = box[ys_sorted_index[0], 1]
    y2 = box[ys_sorted_index[3], 1]
    
    #print "y1,y2",y1,y2

    img_org2 = img.copy()
    img_plate = img_org2[y1:y2, x1:x2]
    #cv2.imshow('number plate', img_plate)
    cv2.imwrite('number_plate.jpg', img_plate)
    
    '''
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow('img', img)
    '''
    
    # 带轮廓的图片
    cv2.imwrite('contours.png', img)
    #cv2.imshow('contours', img_plate)
 
    '''cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    #return img_plate

def Get_hsv_hist(img):
    #input:ROI image
    #output: three value ---hsv
    #得到颜色中最主要的rgb值，采取直方图方法
    imagePath = 'number_plate.jpg'
    img = cv2.imread(imagePath)
    bhist = cv2.calcHist([img],[0],None,[256],[0.0,256.0])
    ghist = cv2.calcHist([img],[1],None,[256],[0.0,256.0])
    rhist = cv2.calcHist([img],[2],None,[256],[0.0,256.0])
    """---------------------------------------------------
    cv2.calcHist中的参数，第一个是图像；第二个如果是0则是
    灰度图，0/1/2分别对应彩色图的bgr通道；第三个None表示全图；
    第四个是bins；第五个是灰度值范围
    ---------------------------------------------------"""
    
    key = 0
    bmax = gmax = rmax = 0
#print "b通道的直方图值",bhist
    #借助冒泡排序
    for i in range(0,256):
        if key < bhist[i] :
            key = bhist[i]
            bmax = i
    for i in range(0,256):
        if key < ghist[i] :
            key = ghist[i]
            gmax = i
    for i in range(0,256):
        if key < rhist[i] :
            key = rhist[i]
            rmax = i
    print "rgb直方图的值:",gmax,rmax,bmax
    #return (bmax,gmax,rmax)

#def RGBtoHSV(b,g,r):   
    #将rgb转为hsv
    #返回的hsv值为小数点后两位数，hsv范围分别是：
    #0-360/0-1/0-1
    #round函数保留小数点后几位，2代表两位
    rs = round(rmax/ 255.0 , 2)  
    gs = round(gmax/ 255.0 , 2)
    bs = round(bmax/ 255.0 , 2)
    
    vs = max(rs,gs,bs)
    vm = min(rs,gs,bs)
    if vs != 0:
        ss = 1 - vm/vs
    else:
        ss = 0
    
    if vs == rs:
        hs = 60 * (gs - bs) / (vs - vm)
    elif vs == gs:
        hs = 120 + 60 * (bs - rs) / (vs - vm)
    else:
        hs = 240 + 60 * (rs - gs) / (vs - vm)
    
    return (round(hs,2),round(ss,2),round(vs,2))

def HSVtoYanse(h,s,v): 
    #这里hsv判断标准的范围是：
    #0-180/0-255/0-255
    
    h = round(h / 2.0 , 1)
    s = round(s * 255)
    v = round(v * 255)  
    yanse = ['black','gray','white','red','yellow','bule','green','purple','brown','pink']

    #黑色
    if v <= 46 :
        return yanse[0]
    #灰色
    elif s <= 43 and v >= 46 and v <= 220:
        return yanse[1]
    #白色
    elif v >= 221 and s <= 30 :
        return yanse[2]
    #红色
    elif h <= 10 or h >= 156:
        return yanse[3]
    #黄色
    elif h >= 26 and h <= 34 and s >= 43 and v >= 46:
        return yanse[4]
    #蓝色
    elif h >= 100 and h <= 124 and s >= 43 and v >= 46:
        return yanse[5]
    #绿色
    elif h >= 35 and h <= 99:
        return yanse[6]
    #紫色
    elif h >= 125 and h <= 155 and s >= 43 and v >= 46:
        return yanse[7]
    #棕色
    else:
        return yanse[8]
    #粉色：暂缺
 
def xianshi(img):
    #bb,gg,rr = Getbgrhist(img)
    hs,ss,vs =  Get_hsv_hist(img)#得到hsv的直方图单值
    ys =  HSVtoYanse(hs,ss,vs)#对hsv进行分类输出颜色
    global YanSe #识别结果用于后面的写入txt文档
    YanSe = ys
    #print "(b g r  的范围是0-255)b g r 的值:",bb,gg,rr
    #print "(hsv的范围分别是0-360°,0-1,0-1)h s v 的值:",hs,ss,vs
    print "hsv直方图的值/颜色:",hs,ss,vs,ys
    #return ys

def zhixing():
    img  = cv2.imread("./linshi/test.jpg") #从临时文件夹读取图像  
    detect(img)#得到ROI区域
    xianshi(img)#显示颜色
    os.remove('./number_plate.jpg')#删除过程中文件，以免影响下一次识别
    os.remove('./contours.png')

def file_name(file_dir):  
        pic_name= []
        for root, dirs, files in os.walk(file_dir):  
        #print(files) #当前路径下所有非目录子文件
            pic_name.append(files)
        return pic_name    
    
def piliangzhixing():
    #用于批量处理
    pic_name= file_name('./tes')#待识别图像文件名字的读取
    for i in range(0,len(pic_name)):
        picture_name= pic_name[i]
        
    #批量读入图像并存在coll
    
    coll = io.ImageCollection('./tes/*.jpg')
    
    print '图片的数量',len(coll)
    
    for i in range(0,len(coll)):
        
        io.imsave('./linshi/test.jpg',coll[i])
        zhixing()
        os.remove('./linshi/test.jpg')
        #print "全局变量YanSe",YanSe
        #识别结果写进去txt
        fp = open('./result/test.txt','a+')
        fp.write(picture_name[i] + ' ' + YanSe + '\n')
        fp.close()
    #修改结果名字txt
    result_txt_name = time.strftime('%Y%m%d_%H_%M',time.localtime(time.time()))
    result_name = result_txt_name + '.txt'    
    os.rename('./result/test.txt', './result/'+ result_name)
    
if __name__ == '__main__':
    piliangzhixing()
    

    
    

