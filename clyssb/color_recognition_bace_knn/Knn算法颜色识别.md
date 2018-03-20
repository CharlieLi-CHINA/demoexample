# Knn算法颜色识别

> from: [https://github.com/ahmetozlu/color_recognition](https://github.com/ahmetozlu/color_recognition)

##说明

这个项目着眼于用RGB颜色直方图来训练KNN机器学习分类器，从而进行颜色分类。其可以分类白色、黑色、红色、绿色、蓝色、橙色、黄色以及紫色。如果想要分类更多颜色或者提高精度，可以修改 training data 以及考虑其他颜色特征 ，比如  [Color Moments](https://en.wikipedia.org/wiki/Color_moments)或者[Color Correlogram ](http://www.cs.cornell.edu/rdz/Papers/ecdl2/spatial.htm)


## 演示

![](https://user-images.githubusercontent.com/22610163/34917659-8497acae-f95a-11e7-93fb-f7cd6cc3128a.gif)


## 程序的做法

1. 特征提取：通过训练图像中的rgb颜色直方图进行特征提取
2. 训练KNN分类器：通过RGB颜色直方图 的值来训练KNN分类器
3. 通过训练KNN来分类：对每一帧进行特征提取，然后通过训练KNN分类器来分类中值颜色

## 理论 

在这里，颜色通过使用KNN机器学习分类器算法进行分类，这个分类器通过训练图像的RGB颜色直方图的值来进行分类，其工作原理框架如下图：

![](https://user-images.githubusercontent.com/22610163/35335133-a9632c70-0125-11e8-9204-0b4bfd0702a7.png)

这里，必须知道两个主要的理论来理解基于目标检测/识别系统的计算机视觉以及机器学习。

1）特征提取

如何在图像中表示我们发现的能与其他点或者特征分得开的兴趣点。

2）分类

一个能实现分类的算法，特别能具体实现分类，其被称为一个分类器。这个“分类器”有时也指数学函数，其通过分类算法的实现，输入的数据映射到一个类别。


对于这个项目

1）特征提取 = 颜色直方图

颜色直方图是一幅图像中颜色分布的表示。对于数字图像，一个颜色直方图代表像素的数量，在每一个固定的列表的颜色范围的颜色，跨越图像的颜色空间，所有可能的颜色集。

![](https://user-images.githubusercontent.com/22610163/34918867-44f5feaa-f96b-11e7-9994-1747846266c9.png)

2）分类器 = KNN算法

K近邻是一个简单的算法，它存储所有可用的案例，并基于相似性度量（例如距离函数）对新案例进行分类。 KNN作为一种非参数技术已经在1970年代初期用于统计估计和模式识别。

![](https://user-images.githubusercontent.com/22610163/34918895-c7b94d24-f96b-11e7-87da-8619d9bd4246.png)


## 实现

这里面的颜色直方图计算和knn分类器会使用opencv，Numpy被使用来矩阵/ N维数组计算。算法在Linux环境下的Python下运行。

- color_classification_main.py: 主程序
- feature_extraction.py: 特征提取程序
- knn_classifier.py: knn分类

1）特征提取程序：

我可以通过这个Python类获取图像的RGB颜色直方图。 例如，红色图像之一的RGB颜色直方图的绘图如下所示。

![](https://user-images.githubusercontent.com/22610163/34919478-f198beb8-f975-11e7-8c1c-0a552f7cd673.jpg)

我决定使用具有R，G和B的像素数的峰值的直方图的bin数作为特征，以便我可以获得主要的R，G和B值以创建用于训练的特征向量。 例如，上面给出的红色图像的主要R，G和B值是[254,0,2]。

我通过使用颜色直方图为每个训练图像获得主导的R，G，B值，然后我标记它们是因为KNN分类器是一个监督学习器，我将这些特征向量部署在csv文件中。 因此，我创建了我的训练特征矢量数据集。 可以在src文件夹下找到名称为training.data的文件。

2.）“knn_classifier.py”的解释

这个课程提供了这些主要计算;

- 获取训练数据
- 获取测试图像功能
- 计算欧氏距离
- 获得k近邻点
- 颜色预测
- 返回预测是对还是错


“color_classification_main.py”是我的程序的主要类，它提供了：

- 调用feature_extraction.py以通过特征提取创建训练数据
- 
- 调用knn_classifier.py进行分类


## 总结

我认为，训练数据在分类准确性方面有着巨大的重要性。 我仔细地创建了我的训练数据，但使用更合适的训练数据可能会提高准确性。

另一个重要的事情是闪电和阴影。 在我的测试图像中，在不良照明条件下拍摄的图像和阴影被分类错误（误报），也许某些滤波算法应该/可以在测试图像发送到KNN分类器之前执行。因此，可以提高准确性。


## 引用

如果您在出版物中使用此代码，请将其引用为：

    @ONLINE{vdtc,
        author = "Ahmet Özlü",
        title  = "Color Classifier",
        year   = "2018",
        url    = "https://github.com/ahmetozlu/color_recognition"
    }

## Author

Ahmet Özlü

## 执照


该系统根据MIT许可证提供。 有关更多信息，请参阅许可证文件。