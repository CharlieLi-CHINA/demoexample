# python安装mlab


- 环境：codna2以及3同时安装，以2为主，3安装在2的envs文件夹下

- 事件原由：由于想要用Python调用matlab模块以及里面的函数（解决IIF那个函数使用的问题），所以就要安装，发现以下问题


- 在py3下，出现安装不了malb的问题，UnicodeDecodeError: 'gbk' codec can't decode byte 0x99 in position 1945: ill这个问题，然后经过百度，找到这个方法https://bbs.csdn.net/topics/392275721，用了之后，发现import时出现 no module named releases问题，又采取清空解压后的mlab包里面的README.rst文件再安装，还是出现releases问题，于是又pip install releases后解决。

        (py3) C:\Users\liqilv>pip install releases
        Collecting releases
          Downloading https://pypi.doubanio.com/packages/91/0d/9aedbc9a8822334363ef4789de206caa196b781d55df9011fb336e17e7d3/releases-1.5.0-py2.py3-none-any.whl
        Collecting semantic-version<3.0 (from releases)
          Downloading https://pypi.doubanio.com/packages/28/be/3a7241d731ba89063780279a5433f5971c1cf41735b64a9f874b7c3ff995/semantic_version-2.6.0-py3-none-any.whl
        Requirement already satisfied: sphinx<1.7,>=1.3 in d:\anaconda2\envs\py3\lib\site-packages\sphinx-1.5.6-py3.6.egg (from releases)
        Requirement already satisfied: six>=1.5 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: Jinja2>=2.3 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: Pygments>=2.0 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: docutils>=0.11 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: snowballstemmer>=1.1 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: babel!=2.0,>=1.3 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: alabaster<0.8,>=0.7 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: imagesize in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: requests>=2.0.0 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: colorama>=0.3.5 in d:\anaconda2\envs\py3\lib\site-packages (from sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: MarkupSafe>=0.23 in d:\anaconda2\envs\py3\lib\site-packages (from Jinja2>=2.3->sphinx<1.7,>=1.3->releases)
        Requirement already satisfied: pytz>=0a in d:\anaconda2\envs\py3\lib\site-packages (from babel!=2.0,>=1.3->sphinx<1.7,>=1.3->relea

- 在py2下，出现错误 no module named win32com.client，无解（开始以为是其出问题，又卸载重新在2的环境下装mlab，用pip很顺利），后来重启cmd再import后可以，后经过测试，发现不能同时py2和py3用mlab，每次只能用一个，然后退出后再用，情况如下：
即，在2的环境下import后，转到3的环境import，这两个可以，但是再转回2的环境下就不用，就出现no module named win32com.client问题------

        (D:\Anaconda2) C:\Users\liqilv>python
        Python 2.7.13 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        Anaconda is brought to you by Continuum Analytics.
        Please check out: http://continuum.io/thanks and https://anaconda.org
        >>> import mlab
        >>> exit()

        (D:\Anaconda2) C:\Users\liqilv>activate py3

        (py3) C:\Users\liqilv>python
        Python 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:25:24) [MSC v.1900 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import mlab
        >>> exit()

        (py3) C:\Users\liqilv>deactivate py3

        C:\Users\liqilv>python
        Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import mlab
        win32com in missing, please install it
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "D:\Python27\lib\site-packages\mlab\__init__.py", line 11, in <module>
            import releases
          File "D:\Python27\lib\site-packages\mlab\releases.py", line 12, in <module>
            from mlabwrap import (MlabWrap, choose_release, find_available_releases,
          File "D:\Python27\lib\site-packages\mlab\mlabwrap.py", line 188, in <module>
            import mlabraw
          File "D:\Python27\lib\site-packages\mlab\mlabraw.py", line 14, in <module>
            from matlabcom import MatlabCom as MatlabConnection
          File "D:\Python27\lib\site-packages\mlab\matlabcom.py", line 19, in <module>
            import win32com.client
        ImportError: No module named win32com.client
        >>>




