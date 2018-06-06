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


## 后续待更新




