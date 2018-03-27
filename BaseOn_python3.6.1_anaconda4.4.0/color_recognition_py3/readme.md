# color_recognition 说明

编程参考
> [https://github.com/ahmetozlu/color_recognition](https://github.com/ahmetozlu/color_recognition)

## 环境

Python3.6.1,用到的库包括: numpy,cv2,time,sys,os,PIL(主要用到Image),skimage,matplotlib,scipy,csv,random,math,operator


## 文件说明

### ./result    存放识别结果的txt文档
###  ./test_picture    测试图像文件夹
###  ./training_dateset    训练样本文件夹
###  test.data    最新一次的测试获得的图像rgb直方图值
###  training.data    颜色分类范围文件
###  knn_classifier.py knn分类
###  color_histogram_feature_extraction.py 特征提取程序
###  0326i_color_classification_main.py 主程序


## 运行

### 总的思路

1. 特征提取：通过训练图像中的rgb颜色直方图进行特征提取
2. 训练KNN分类器：通过RGB颜色直方图 的值来训练KNN分类器
3. 通过训练KNN来分类：对图像进行特征提取，然后通过训练KNN分类器来分类中值颜色

### 具体执行

- 首次运行需要执行 knn_classifier.py
以及color_histogram_feature_extraction.py文件
即：
> 调用feature_extraction.py以通过特征提取创建训练数据

> 调用knn_classifier.py进行分类

- 然后执行主程序

- 从 ./test_picture加载图像，执行for循环时，
每次读入的图像先保存为test.jpg(test后面或许有后缀，如test1.jpg），
经过裁剪后保存为linshi.jpg，经过knn识别后（就是上面加载的那两个.py文件）输出预测结果，并写在图像上输出，然后下一个。


### 额外

“knn_classifier.py”的解释

这个程序提供了这些主要计算;

- 获取训练数据
- 获取测试图像功能
- 计算欧氏距离
- 获得k近邻点
- 颜色预测
- 返回预测是对还是错



## 理论

在这里，颜色通过使用KNN机器学习分类器算法进行分类，这个分类器通过训练图像的RGB颜色直方图的值来进行分类，其工作原理框架如下图：
![](https://user-images.githubusercontent.com/22610163/35335133-a9632c70-0125-11e8-9204-0b4bfd0702a7.png)


