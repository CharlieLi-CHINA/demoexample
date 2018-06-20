# 这里主要分享自己的一些在python编程方面的一些做法和遇到的问题

- 编程环境：anaconda2为主，里面的envs文件夹安装有conda3，在命令行用到Python时，py2和3转换时需要在命令行activate py3以及deactivate py3即可

## 2018.05.30问题--Spyder

之前一直用Spyder都可以，但是这次在py3下就出现问题“name 'runfile' is not defined”，可能是用了jupyter的问题，于是我关掉jupyter，又重启电脑，还是不行，最后在anaconda里面重装Spyder即可，解决办法看：http://baijiahao.baidu.com/s?id=1593805287870847702&wfr=spider&for=pc ，简单粗暴有效。
![](https://i.imgur.com/joaFBoo.png)
![](https://i.imgur.com/qGPAIkM.png)

## 2018.06.04 ocr，tesseract问题

准备进行ocr 的识别，接到同事的demo后，想运行，要在python2上pip安装pytesseract，安装完毕并，运行后，发现出现错误：

> UnicodeDecodeError: 'ascii' codec can't decode byte 0xe9 in position 70: ordinal not in range(128)

退出去Spyder后，用命令行执行，发现又出现问题：

> (D:\Anaconda2) C:\Users\liqilv>d:

> (D:\Anaconda2) D:\>cd D:\Anaconda2\liqilv_bigdata_engineer_collage\bankcard_read

> (D:\Anaconda2) D:\Anaconda2\liqilv_bigdata_engineer_collage\bankcard_read>python image_split.py
Traceback (most recent call last):
  File "image_split.py", line 107, in <module>
    print yinhang_number(img)
  File "image_split.py", line 35, in yinhang_number
    img=cv2.resize(img, (1200, int(hight*1./width*1200)), cv2.INTER_AREA)#閲嶆柊璋冩暣鍥剧墖澶у皬 锛屽師鏉ョ殑
TypeError: dst is not a numpy array, neither a scalar

> (D:\Anaconda2) D:\Anaconda2\liqilv_bigdata_engineer_collage\bankcard_read>


经同事提醒，我的Python2装的是cv是2.4版本，而他的是3.4，这个有点不一样，就是2的版本不是当数组在用，所以我又在3下运行，发现缺少个tesseract引擎，原来发现要先下一个引擎，再调用的，而不仅仅是在python库里面调用，之后我百度如何安装tesseract引擎，后来总算是可以运行同事的程序了。

除此外，晚上回来后由于要完成实验室的项目，所以要搜集图像，然后标注，这个过程中需要命名为标注的信息以及裁剪，所以晚上又查了自己的以前的代码，改进下，争取做个能做到区域截图、自动命名的小脚本，而自己也有了用脚本来替代人工的想法，不想做那些重复性工作。

## 20180606 h5py问题

在import tensorflow以及t5py时遇到问题：

> D:\Anaconda2\envs\py3\lib\site-packages\h5py\__init__.py:34: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters

解决办法

直接pip安装 
> pip install h5py==2.8.0rc1，但是又出现新问题 

> [WinError 17] 系统无法将文件移到不同的磁盘驱动器 的问题

以至于装错，所以解决的新办法是：
在C:\Windows\System32下的cmd管理员运行cmd.exe，然后在py3的环境（activate py3）下

> pip install h5py==2.8.0rc1 --user

问题解决了


> C:\WINDOWS\system32>activate py3

> (py3) C:\WINDOWS\system32>pip install h5py==2.8.0rc1 --user
> Collecting h5py==2.8.0rc1
  Downloading https://pypi.doubanio.com/packages/9e/cf/a6e35cc6273c8be51f3b02cc2aac73ab15e9e41338e1a3cb46118650de8c/h5py-2.8.0rc1-cp36-cp36m-win_amd64.whl (2.3MB)
    100% |████████████████████████████████| 2.3MB 422kB/s
Requirement already satisfied: six in d:\anaconda2\envs\py3\lib\site-packages (from h5py==2.8.0rc1)
Requirement already satisfied: numpy>=1.7 in d:\anaconda2\envs\py3\lib\site-packages (from h5py==2.8.0rc1)
Installing collected packages: h5py
Successfully installed h5py-2.8.0rc1
You are using pip version 9.0.1, however version 10.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

> (py3) C:\WINDOWS\system32>


之后，问题解决了。


## 20180607周四 装深度学习框架问题

第一个问题是pip install pytorch问题，由于pip里面没有相应的东西，所以只能走官网途径，通过pip官网提供的网址进行下载安装，并顺便pip install torchvision，如下

    pip install http://download.pytorch.org/whl/cpu/torch-0.4.0-cp36-cp36m-win_amd64.whl 
    pip install torchvision

这个问题其实解决的不算啥；

第二个问题是安装lmdb，这个也用pip安装，也能下载，但是到了最后阶段会有个问题，就是这个

> error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual 

也去网上搜了下，都是主张自己去下载相应whl文件回来再pip安装，所以下载完后，我就cd到这个文件目录，再pip安装，如下：

    pip install lmdb-0.94-cp36-cp36m-win_amd64.whl

而在找的时候发现，不能直接找lmdb这个模块，而是要找pylmdb，否则找不到。

其实遇到这类问题，可以先自己上这个网站[https://www.lfd.uci.edu/~gohlke/pythonlibs/](https://www.lfd.uci.edu/~gohlke/pythonlibs/) 上去找有么有相应的whl文件，再在文件所在目录pip安装即可

以上都是安装依赖包的问题，其实还有个问题，就是今天在试着跑rcnn.pytorch里面的demo-edit.Py文件时，发现有个问题，其出现的错误最后是：

> AttributeError: module 'torch._C' has no attribute '_cuda_getDevice'

我分析下，因为这个模型训练用gpu，而我是在cpu的环境下，pytorch也是cpu版本，所以就会出错，刚好google搜到个同样的[问题](https://www.google.com.hk/search?q=AttributeError%3A+module+%27torch._C%27+has+no+attribute+%27_cuda_getDevice%27&oq=AttributeError%3A+module+%27torch._C%27+has+no+attribute+%27_cuda_getDevice%27&aqs=chrome..69i57j69i58j69i60l3.242j0j4&sourceid=chrome&ie=UTF-8)，所以解决了，[办法](https://github.com/pytorch/pytorch/issues/5286)参考如下：

将类似于语句

    model.load_state_dict(torch.load(file))
改为

    model.load_state_dict(torch.load(file, map_location='cpu'))
即可

也可以在cpu版本下跑gpu训练好的模型

## 20180608周五 ctpn运行

ctpn运行出问题（未解决）：


    runfile('D:/Anaconda2/envs/py3/liqilv_bigdata_engineer_py3/text-detection-ctpn/ctpn/demo.py', wdir='D:/Anaconda2/envs/py3/liqilv_bigdata_engineer_py3/text-detection-ctpn/ctpn')
    Traceback (most recent call last):

      File "<ipython-input-16-991feae81c3c>", line 1, in <module>
        runfile('D:/Anaconda2/envs/py3/liqilv_bigdata_engineer_py3/text-detection-ctpn/ctpn/demo.py', wdir='D:/Anaconda2/envs/py3/liqilv_bigdata_engineer_py3/text-detection-ctpn/ctpn')

      File "D:\Anaconda2\envs\py3\lib\site-packages\spyder\utils\site\sitecustomize.py", line 688, in runfile
        execfile(filename, namespace)

      File "D:\Anaconda2\envs\py3\lib\site-packages\spyder\utils\site\sitecustomize.py", line 101, in execfile
        exec(compile(f.read(), filename, 'exec'), namespace)

      File "D:/Anaconda2/envs/py3/liqilv_bigdata_engineer_py3/text-detection-ctpn/ctpn/demo.py", line 8, in <module>
        from lib.networks.factory import get_network

      File "D:\Anaconda2\envs\py3\liqilv_bigdata_engineer_py3\text-detection-ctpn\lib\__init__.py", line 1, in <module>
        from . import fast_rcnn

      File "D:\Anaconda2\envs\py3\liqilv_bigdata_engineer_py3\text-detection-ctpn\lib\fast_rcnn\__init__.py", line 2, in <module>
        from . import train

      File "D:\Anaconda2\envs\py3\liqilv_bigdata_engineer_py3\text-detection-ctpn\lib\fast_rcnn\train.py", line 5, in <module>
        from ..roi_data_layer.layer import RoIDataLayer

      File "D:\Anaconda2\envs\py3\liqilv_bigdata_engineer_py3\text-detection-ctpn\lib\roi_data_layer\__init__.py", line 1, in <module>
        from . import roidb

      File "D:\Anaconda2\envs\py3\liqilv_bigdata_engineer_py3\text-detection-ctpn\lib\roi_data_layer\roidb.py", line 5, in <module>
        from lib.utils.bbox import bbox_overlaps

      File "D:\Anaconda2\envs\py3\liqilv_bigdata_engineer_py3\text-detection-ctpn\lib\utils\__init__.py", line 4, in <module>
        from . import bbox

      File "D:\Anaconda2\envs\py3\lib\site-packages\pyximport\pyximport.py", line 445, in load_module
        language_level=self.language_level)

      File "D:\Anaconda2\envs\py3\lib\site-packages\pyximport\pyximport.py", line 232, in load_module
        raise exc.with_traceback(tb)

      File "D:\Anaconda2\envs\py3\lib\site-packages\pyximport\pyximport.py", line 216, in load_module
        inplace=build_inplace, language_level=language_level)

      File "D:\Anaconda2\envs\py3\lib\site-packages\pyximport\pyximport.py", line 192, in build_module
        reload_support=pyxargs.reload_support)

      File "D:\Anaconda2\envs\py3\lib\site-packages\pyximport\pyxbuild.py", line 102, in pyx_to_dll
        dist.run_commands()

      File "D:\Anaconda2\envs\py3\lib\distutils\dist.py", line 955, in run_commands
        self.run_command(cmd)

      File "D:\Anaconda2\envs\py3\lib\distutils\dist.py", line 974, in run_command
        cmd_obj.run()

      File "D:\Anaconda2\envs\py3\lib\site-packages\Cython\Distutils\old_build_ext.py", line 185, in run
        _build_ext.build_ext.run(self)

      File "D:\Anaconda2\envs\py3\lib\distutils\command\build_ext.py", line 339, in run
        self.build_extensions()

      File "D:\Anaconda2\envs\py3\lib\site-packages\Cython\Distutils\old_build_ext.py", line 193, in build_extensions
        self.build_extension(ext)

      File "D:\Anaconda2\envs\py3\lib\distutils\command\build_ext.py", line 533, in build_extension
        depends=ext.depends)

      File "D:\Anaconda2\envs\py3\lib\distutils\_msvccompiler.py", line 304, in compile
        self.initialize()

      File "D:\Anaconda2\envs\py3\lib\distutils\_msvccompiler.py", line 197, in initialize
        vc_env = _get_vc_env(plat_spec)

      File "D:\Anaconda2\envs\py3\lib\distutils\_msvccompiler.py", line 85, in _get_vc_env
        raise DistutilsPlatformError("Unable to find vcvarsall.bat")

    ImportError: Building module lib.utils.bbox failed: ['distutils.errors.DistutilsPlatformError: Unable to find vcvarsall.bat\n']



主要是出现 
> ImportError: Building module lib.utils.bbox failed: ['distutils.errors.DistutilsPlatformError: Unable to find vcvarsall.bat\n']
问题，经过搜索，一个可能是vs版本要14以上，也即是要装个15版本的，还有就是注册表那里要编辑

查看 链接  [1](https://jingyan.baidu.com/article/adc815138162e8f723bf7387.html)    [2](https://blog.csdn.net/donger_soft/article/details/44838109)  



## 20180611周一 装双系统win10+deepin

由于要跟同事的开发环境一致，不得不装个双系统，在ubuntu和deepin之间考虑了下，并且目睹了一位同事在ubuntu上装东西各种报错，最后还是决定装deepin了。

步骤

- 分区（[教程](https://jingyan.baidu.com/article/425e69e6bbd0c7be14fc164a.html)），这个简单，在win10里面的搜索框里面搜索  磁盘  ，会出现个 创建并格式化硬盘分区 ，然后点击去即可以，同样，也可以在控制面板找到这个东西；然后按照下图所示，在你想要创建分区的盘里面 压缩卷 并设好大小 ，待出现个未分配的磁盘分区后，新建简单卷，然后给定容量，就可以很容易地弄好分区了。

![](http://img.xitongcheng.com/upload/image/20160107/20160107171106_42992.jpg)
![](http://img.xitongcheng.com/upload/image/20160107/20160107171117_30780.jpg)
![](http://img.xitongcheng.com/upload/image/20160107/20160107171131_45277.jpg)
由于这个分区是给装deepin，所以就没有弄分配的磁盘盘符，故而新建个简单卷就可以了。

- 分完区，然后就是关闭win10的快速启动，教程可以看[这里](https://jingyan.baidu.com/article/48b558e30ca7977f38c09a95.html) ，简单来说，就是在电源设置那里的电源选项界面将快速启动关闭而已，以免等下重启电脑的时候默认启动windows而不是U盘。
- 这里直接弄个U盘启动即可，有个U盘启动，然后开机时进入bios，我的是华硕，所以同时f2或者f10、f12进入，好像忘了哪一个，反正百度下即可；接下来即是选语言之类的，傻瓜式安装，然后重启，选择进入deepin（通常是第一个系统，windows还在它下面）即可。当然了，密码什么的要设好。

使用

感觉界面挺清爽，和mac有的一拼，直观上比ubuntu好用一点点。

然后就是各种安装了，一开始就要装pycharm，同事说做工程还是不错的，而且可以和服务器联机运行之类的，社区版本免费，专业版淘宝很便宜。

相比于windows，它装python的库是挺方便的。
而在opencv来说，它可以本地编译，然后各种功能比较齐全，参考[链接](http://www.cnblogs.com/arkenstone/p/6490017.html) 。
然后是cmake

    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python -c "import sys; print sys.prefix") -D PYTHON_EXECUTABLE=$(which python) -D OPENCV_EXTRA_MODULES_PATH=/opt/opencv/opencv_contrib/modules -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_CUDA=OFF -D INSTALL_PYTHON_EXAMPLES=OFF ..

当然了，也要具体情况具体调整

    charlie@charlie-PC:~/Desktop/opencv$ sudo mv opencv/ /opt
    [sudo] charlie 的密码：
    charlie@charlie-PC:~/Desktop/opencv$ cd /opt/opencv
    charlie@charlie-PC:/opt/opencv$ mkdir build
    charlie@charlie-PC:/opt/opencv$ cd build/
    charlie@charlie-PC:/opt/opencv/build$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D PYTHON_EXECUTABLE=$(which python3) -D OPENCV_EXTRA_MODULES_PATH=/opt/opencv/opencv_contrib/modules -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_CUDA=OFF -D INSTALL_PYTHON_EXAMPLES=OFF ..
    -- The CXX compiler identification is GNU 6.4.0
    -- The C compiler identification is GNU 6.4.0
    -- Check for working CXX compiler: /usr/bin/c++
    -- Check for working CXX compiler: /usr/bin/c++ -- works
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Check for working C compiler: /usr/bin/cc
    -- Check for working C compiler: /usr/bin/cc -- works
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Performing Test HAVE_CXX11 (check file: cmake/checks/cxx11.cpp)
    -- Performing Test HAVE_CXX11 - Success
    -- Found PythonInterp: /usr/bin/python3 (found suitable version "3.5.4", minimum required is "2.7") 
    -- Found PythonInterp: /usr/bin/python3 (found suitable version "3.5.4", minimum required is "3.4") 
    -- Found PythonLibs: /usr/lib/x86_64-linux-gnu/libpython3.5m.so (found suitable exact version "3.5.4rc1") 
    -- Looking for ccache - not found
    -- Performing Test HAVE_CXX_FSIGNED_CHAR
    -- Performing Test HAVE_CXX_FSIGNED_CHAR - Success
    -- Performing Test HAVE_C_FSIGNED_CHAR
    -- Performing Test HAVE_C_FSIGNED_CHAR - Success
    -- Performing Test HAVE_CXX_W
    -- Performing Test HAVE_CXX_W - Success
    -- Performing Test HAVE_C_W
    -- Performing Test HAVE_C_W - Success
    -- Performing Test HAVE_CXX_WALL
    -- Performing Test HAVE_CXX_WALL - Success
    -- Performing Test HAVE_C_WALL
    -- Performing Test HAVE_C_WALL - Success
    -- Performing Test HAVE_CXX_WERROR

将解压后的opencv文件去掉master，将其扩展移进去里面，然后将它整体移到opt文件夹，建立build文件夹，在里面编译，cmake，详细见上面的改进。

    charlie@charlie-PC:~/Downloads$ sudo pip3 install lmdb-0.94-cp35-cp35m-win_amd64.whl 
    lmdb-0.94-cp35-cp35m-win_amd64.whl is not a supported wheel on this platform.
    charlie@charlie-PC:~/Downloads$ cd ..
    charlie@charlie-PC:~$ sudo pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple lmdb
    Collecting lmdb
      Downloading https://pypi.tuna.tsinghua.edu.cn/packages/cb/31/5be8f436b56733d9e69c721c358502f4d77b627489a459978686be7db65f/lmdb-0.94.tar.gz (4.0MB)
        100% |████████████████████████████████| 4.0MB 173kB/s 
    Building wheels for collected packages: lmdb
      Running setup.py bdist_wheel for lmdb ... done
      Stored in directory: /root/.cache/pip/wheels/bf/c8/0f/327d1a7ade5ae087c242d80f079a899c2ab842dbbd6c1a53a1
    Successfully built lmdb
    Installing collected packages: lmdb
    Successfully installed lmdb-0.94
    charlie@charlie-PC:~$ 

linux安装lmdb不像Windows那样子，直接pip就可以

还有，装tesseract也是，好像是直接pip3还是apt就可以，挺方便。


## 20180613周三 img操作问题

在运行同事的代码，然后自己改进下，想要找到所有保卫框中坐标最大的那个（对应着身份证数字），然后想要保存此坐标，自己做个裁剪图算法验证下，然后发现，我使用原来的输入图像进行切片，发现总与ctpn做的切片得到的片段不一样，后来自己将ctpn运行过程中的图像进行鼠标选点显示坐标，发现看似一样的两幅图（原图与ctpn处理后的图）同一个地方的坐标点相差一百多两百，怪不得使用其坐标没有什么作用，对应不上。后来在查看ctpn的文件时，在其**./ctpn/ctpn/model.py**发现下面代码：

        # 进行文本识别
    def ctpn(img):
        """
        text box detect
        """
        scale, max_scale = Config.SCALE, Config.MAX_SCALE
        # 对图像进行resize，输出的图像长宽
        img, f = resize_im(img, scale=scale, max_scale=max_scale)
        scores, boxes = test_ctpn(sess, net, img)
        return scores, boxes, img
原来对输入的图像是做一个变换的，而我的裁剪代码：

    def cut_guding(path):
        img = cv2.imread(path)
        boxx = [496, 646, 1024, 658, 495, 688, 1024, 700]
        boxx = np.array(boxx)
        x = np.sort([boxx[0], boxx[2], boxx[4], boxx[6]])

        y = np.sort([boxx[1], boxx[3], boxx[5], boxx[7]])

        cv2.imwrite("lihsi.jpg", img[y[0]:y[-1], x[0]:x[-1], :])
        print(img.shape[:2])
        
    
以及

    #coding=utf-8
    from ctpn.text_detect import text_detect
    import cv2
    import os
    import sys
    from math import *
    # sys.path.insert(0, '/home/walker/PycharmProjects/ctpn_crnn/crnnpytorch')
    # import demoedit
    import numpy as np



    def sort_box(box):
        """
        对box排序,及页面进行排版
        text_recs[index, 0] = x1
            text_recs[index, 1] = y1
            text_recs[index, 2] = x2
            text_recs[index, 3] = y2
            text_recs[index, 4] = x3
            text_recs[index, 5] = y3
            text_recs[index, 6] = x4
            text_recs[index, 7] = y4
        """

        box = sorted(box, key=lambda x: sum([x[1], x[3], x[5], x[7]]))
        sum_0 = 0
        #print("box lenth",len(box),box[0])
        for i in range(0,len(box)): #寻找身份证数字那一栏的保卫框，以纵坐标为sum
            sum_x = box[i][0]+box[i][2]+box[i][4]+box[i][6]
            if (sum_x > sum_0):
                sum_0 = sum_x
                box_max = i
            print("sum_x_of_box)",sum_x)
        print("max box",box[box_max])
        return box

    def image_split(img, text_recs):
        images=[]
        text_recs=sort_box(text_recs)
        text_recs=np.array(text_recs)
        i=0
        for text_rec in text_recs:
            x = np.sort(text_rec[[0,2,4,6]])
            y = np.sort(text_rec[[1,3,5,7]])
            x[x<0]=0
            y[y<0]=0
            images.append(img[y[0]:y[-1], x[0]:x[-1], :])
            cv2.imwrite(os.path.join("picresults", str(i)+".jpg"), img[y[0]:y[-1], x[0]:x[-1], :])
            i+=1
    def picture_rotate(image):

        #image = cv2.imread(path)
        #cv2.imshow("original",image)
        
        height,width = image.shape[:2]
        center = (width // 2, height // 2)
        degree = 90  # 旋转角度,负数表示顺时针,正数表示逆时针
        # 旋转后的尺寸
        heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
        widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
        #center = (0,0)

        M = cv2.getRotationMatrix2D(center,degree,1.0)
        M[0, 2] += (widthNew - width) / 2  # 重点在这步，目前不懂为什么加这步
        M[1, 2] += (heightNew - height) / 2  # 重点在这步

        rotated = cv2.warpAffine(image,M,(widthNew,heightNew),borderValue=(255,255,255))

        #cv2.imshow('Rotated by' + ' ' + str(degree) +' ' + 'degrees',rotated)
        cv2.imwrite("rotated.jpg",rotated)

        #cv2.waitKey(0)
        return rotated
    #测试图像
    #path="./test2.png"
    path="./23.jpg"
    # path = "营业执照1.jpg"

    img=cv2.imread(path)
    h,w = img.shape[:2]
    print("h,w",h,w)
    #if (h > w):
        #img = picture_rotate(img)#如果图片是竖过来的，就旋转过来
    text_recs, tmp, img=text_detect(img)#经过这个操作，刚开始读入的img是会在在这一步做一个缩放的
    #print(text_recs[0][0])
    image_split(img, text_recs)
    box_xy = sort_box(text_recs)

    #print(sort_box(text_recs))
    print(box_xy)
    cv2.imwrite("tmptest.jpg", tmp)
    cv2.imwrite("imgtest.jpg", img)

发现果然如此，我自己得到的是ctpn处理后的图像


经过此次教训，下次在开发时应多注意下


## 问题 20180619周二

标签（空格分隔）： 未分类


目的是想将经过ctpn切割后的包含文字的图像中两边空白的区域去掉，然后计划使用投影法统计各列元素，确定切割坐标点，但是对一张图可以，对另外一张图不可以；单张图可以，一堆图不行，不知道为什么。

    /usr/bin/python3.5 /home/charlie/Desktop/liqilv_bigdata_engineer_py3/test/0612.py
    OpenCV Error: Assertion failed (scn == 3 || scn == 4) in cvtColor, file /opt/opencv/modules/imgproc/src/color.cpp, line 11048
    ./testpicture/2.jpg
    Traceback (most recent call last):
    ./testpicture/1.jpg
    ./testpicture/7.jpg
      File "/home/charlie/Desktop/liqilv_bigdata_engineer_py3/test/0612.py", line 380, in <module>
    ./testpicture/8.jpg
        touying(path1)
    ./testpicture/3.jpg
      File "/home/charlie/Desktop/liqilv_bigdata_engineer_py3/test/0612.py", line 225, in touying
        GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将BGR图转为灰度图
    ./testpicture/0.jpg
    ./testpicture/4.jpg
    cv2.error: /opt/opencv/modules/imgproc/src/color.cpp:11048: error: (-215) scn == 3 || scn == 4 in function cvtColor
    ./testpicture/6.jpg

    ./testpicture/5.jpg


要不然就是像这样子


    charlie@charlie-PC:~/Desktop/ctpn_crnn$ python3 ctpn_test.py 身份证8.jpg
      File "ctpn_test.py", line 255
        img2.save(path_file,,'jpeg')
                            ^
    SyntaxError: invalid syntax
    charlie@charlie-PC:~/Desktop/ctpn_crnn$ python3 ctpn_test.py 身份证8.jpg
    Tensor("Placeholder:0", shape=(?, ?, ?, 3), dtype=float32)
    Tensor("conv5_3/conv5_3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_conv/3x3/rpn_conv/3x3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_cls_score/Reshape_1:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_cls_prob:0", shape=(?, ?, ?, ?), dtype=float32)
    Tensor("Reshape_2:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_bbox_pred/Reshape_1:0", shape=(?, ?, ?, 40), dtype=float32)
    Tensor("Placeholder_1:0", shape=(?, 3), dtype=float32)
    2018-06-19 20:38:42.979780: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
    Traceback (most recent call last):
      File "ctpn_test.py", line 311, in <module>
        main_process(abspath + path)
      File "ctpn_test.py", line 278, in main_process
        delete_none_words_zone("./picresults")
      File "ctpn_test.py", line 248, in delete_none_words_zone
        x1, x2 = get_words_space(path_file)
      File "ctpn_test.py", line 98, in get_words_space
        if number_zeros > 15 and a[i+1] > 0:
    IndexError: list index out of range
    charlie@charlie-PC:~/Desktop/ctpn_crnn$ python3 ctpn_test.py 身份证8.jpg
    Tensor("Placeholder:0", shape=(?, ?, ?, 3), dtype=float32)
    Tensor("conv5_3/conv5_3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_conv/3x3/rpn_conv/3x3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_cls_score/Reshape_1:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_cls_prob:0", shape=(?, ?, ?, ?), dtype=float32)
    Tensor("Reshape_2:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_bbox_pred/Reshape_1:0", shape=(?, ?, ?, 40), dtype=float32)
    Tensor("Placeholder_1:0", shape=(?, 3), dtype=float32)
    2018-06-19 20:40:39.835308: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
    Traceback (most recent call last):
      File "ctpn_test.py", line 311, in <module>
        main_process(abspath + path)
      File "ctpn_test.py", line 278, in main_process
        delete_none_words_zone("./picresults")
      File "ctpn_test.py", line 248, in delete_none_words_zone
        x1, x2 = get_words_space(path_file)
      File "ctpn_test.py", line 98, in get_words_space
        if number_zeros > 10 and a[i+1] > 0:
    IndexError: list index out of range
    charlie@charlie-PC:~/Desktop/ctpn_crnn$ python3 ctpn_test.py 身份证8.jpg
    Tensor("Placeholder:0", shape=(?, ?, ?, 3), dtype=float32)
    Tensor("conv5_3/conv5_3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_conv/3x3/rpn_conv/3x3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_cls_score/Reshape_1:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_cls_prob:0", shape=(?, ?, ?, ?), dtype=float32)
    Tensor("Reshape_2:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_bbox_pred/Reshape_1:0", shape=(?, ?, ?, 40), dtype=float32)
    Tensor("Placeholder_1:0", shape=(?, 3), dtype=float32)
    2018-06-19 20:45:11.035295: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
    Traceback (most recent call last):
      File "ctpn_test.py", line 313, in <module>
        main_process(abspath + path)
      File "ctpn_test.py", line 280, in main_process
        delete_none_words_zone("./picresults")
      File "ctpn_test.py", line 250, in delete_none_words_zone
        x1, x2 = get_words_space(path_file)
      File "ctpn_test.py", line 99, in get_words_space
        if number_zeros > 15 and a[i + 1] > 0:
    IndexError: list index out of range
    charlie@charlie-PC:~/Desktop/ctpn_crnn$ python3 ctpn_test.py 身份证8.jpg
    Tensor("Placeholder:0", shape=(?, ?, ?, 3), dtype=float32)
    Tensor("conv5_3/conv5_3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_conv/3x3/rpn_conv/3x3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_cls_score/Reshape_1:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_cls_prob:0", shape=(?, ?, ?, ?), dtype=float32)
    Tensor("Reshape_2:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_bbox_pred/Reshape_1:0", shape=(?, ?, ?, 40), dtype=float32)
    Tensor("Placeholder_1:0", shape=(?, 3), dtype=float32)
    2018-06-19 20:49:56.450830: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Traceback (most recent call last):
      File "ctpn_test.py", line 313, in <module>
        main_process(abspath + path)
      File "ctpn_test.py", line 280, in main_process
        delete_none_words_zone("./picresults")
      File "ctpn_test.py", line 250, in delete_none_words_zone
        x1, x2 = get_words_space(path_file)
      File "ctpn_test.py", line 99, in get_words_space
        if number_zeros > 15 and a[i + 1] > 0:
    IndexError: list index out of range
    charlie@charlie-PC:~/Desktop/ctpn_crnn$ python3 ctpn_test.py 身份证8.jpg
    Tensor("Placeholder:0", shape=(?, ?, ?, 3), dtype=float32)
    Tensor("conv5_3/conv5_3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_conv/3x3/rpn_conv/3x3:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("lstm_o/Reshape_2:0", shape=(?, ?, ?, 512), dtype=float32)
    Tensor("rpn_cls_score/Reshape_1:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_cls_prob:0", shape=(?, ?, ?, ?), dtype=float32)
    Tensor("Reshape_2:0", shape=(?, ?, ?, 20), dtype=float32)
    Tensor("rpn_bbox_pred/Reshape_1:0", shape=(?, ?, ?, 40), dtype=float32)
    Tensor("Placeholder_1:0", shape=(?, 3), dtype=float32)
    2018-06-19 20:54:46.104176: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Traceback (most recent call last):
      File "ctpn_test.py", line 315, in <module>
        main_process(abspath + path)
      File "ctpn_test.py", line 282, in main_process
        delete_none_words_zone("./picresults")
      File "ctpn_test.py", line 252, in delete_none_words_zone
        x1, x2 = get_words_space(path_file)
      File "ctpn_test.py", line 99, in get_words_space
        if number_zeros > 15 and a[i + 1] > 0:
    IndexError: list index out of range

这个问题还没有解决，因为空格很难去掉，即：二值化处理那里以及图像长度问题，有时候会困扰很多，导致没办法做成。所以这一想法是暂时放弃了，目前的方向是在ctpn分割前或者crnn识别后进行个预处理或者后处理，而中间的东西，如果没有改变那个网络结构，我想暂时是不能够完成这个工作的。除非自己理解了这个网络，然后训练出个自己的东西，否则现在只能进行微调而不能大的变动。



##  问题20180620周三


for循环做出投影图情形


    /usr/bin/python3.5 /home/charlie/Desktop/liqilv_bigdata_engineer_py3/test/0612.py
    ./testpicture/0.jpg
    ./testpicture/6.jpg
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 3, 2, 0, 0, 0, 2, 2, 0, 0, 1, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    The program 'img' received an X Window System error.
    This probably reflects a bug in the program.
    The error was 'BadWindow (invalid Window parameter)'.
      (Details: serial 12956 error_code 3 request_code 15 minor_code 0)
      (Note to programmers: normally, X errors are reported asynchronously;
       that is, you will receive the error a while after causing it.
       To debug your program, run it with the --sync command line
       option to change this behavior. You can then get a meaningful
       backtrace from your debugger if you break on the gdk_x_error() function.)

    Process finished with exit code 1


后来看了下，做了下实验，发现是图像的路径问题。

## 后续待更新


