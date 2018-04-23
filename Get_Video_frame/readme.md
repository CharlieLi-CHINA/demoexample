# 视频截帧 #

## 开发要求 ##

输入一段视频流，截取视频流中含有车辆的视频帧并保存下来，车辆要尽可能地包含在图像中


## 可能实现的一些方案 ##

### 帧间差分法 ###

采用帧间差分法，利用图像序列中相邻两帧或者三帧图像对应像素值相减，然后取差值图像进行阈值化处理提取出图像中的运动区域。

### 光流法 ###

采用光流法，光流(optical flow)法是空间运动物体在观测成像面上的像素运动的瞬时速度。物体在运动的时候，它在图像上对应点的亮度模式也在做相应的运动，这种图像亮度模式的表观运动就是光流。光流的研究就是利用图像序列中像素的强度数据的时域变化和相关性来确定各自像素位置的“运动”。


### 其他方法 ###

采用轮廓比对的方法，即对视频流间隔一段时间取帧，然后提取轮廓并进行排除，确定图像帧中有车辆的轮廓后进行截帧保存。


## 参考资料&&代码 ##

### 光流法

[光流法介绍1](https://blog.csdn.net/zouxy09/article/details/8683859)

[光流法介绍2](http://www.cnblogs.com/gnuhpc/archive/2012/12/04/2802124.html)

[光流法介绍3](https://blog.csdn.net/on2way/article/details/48953975)

[光流法实现](https://blog.csdn.net/gjy095/article/details/9226883)



### 帧间差分法

[介绍](https://blog.csdn.net/asklw/article/details/53790581)



[参考代码](https://blog.csdn.net/dbvasp/article/details/79094806)

[matlab代码参考
](https://blog.csdn.net/xingor/article/details/50711478)

[小案例](https://www.jianshu.com/p/58c6ca1b66af)

[小案例2](https://www.jianshu.com/p/12533816eddf)

#### 其他

[移动目标检测](https://blog.csdn.net/u013055678/article/details/79389516)

[小案例](http://python.jobbole.com/81593/)

[小案例2](https://blog.csdn.net/lwplwf/article/details/72934468)

[小案例3](http://zhaoxuhui.top/blog/2017/06/28/%E5%9F%BA%E4%BA%8EPython%E7%9A%84OpenCV%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%8617.html#)
