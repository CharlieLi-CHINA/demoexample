# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:20:02 2017

@author: liqilv
function:Matplotlib Tutorial
from: http://reverland.org/python/2012/09/07/matplotlib-tutorial/
"""
from pylab import *

X = np.linspace(-np.pi, np.pi,256,endpoint=True)
#X现在是一个numpy数组，包含从-π到+π(包含π)等差分布的256个值

C,S = np.cos(X), np.sin(X)
#C是正弦(256个值)，S是余弦(256个值)

figure(figsize=(10,6),dpi=100)
#figsize=(10,2)是长宽比，dpi=100是图片大小

plot(X,C,color="red",linewidth=2,linestyle="-",label="cosine")
plot(X,S,color="yellow",label="sine")
legend(loc='upper left')
#linewidth=1.5貌似是默认的线条宽度，这个如果不改就不用写上去，改就写上去
#linestyle="--"是线条形态，"-"表示实线,"--"表示虚线
#label="cosine"添加图例，后面还要加上其位置：legend(loc='upper left')

xlim(X.min()*1.2, X.max()*1.2)
ylim(C.min()*1.2, C.max()*1.2)
#上面两行用来调整图中的线条的边界，防止太宽或者太窄以致不能显示文字

xticks( [-np.pi,-3*np.pi/4, -np.pi/2, -np.pi/4,0, np.pi/4, np.pi/2,3*np.pi/4, np.pi],
       [r'$-\pi$',  r'$-3\pi/4$',r'$-\pi/2$',r'$-\pi/4$', r'$0$',r'$\pi/4$', r'$+\pi/2$', 
        r'$+3\pi/4$', r'$+\pi$'])
yticks([-1,-0.707, 0,0.707, +1],[r'$-1$', r'$-squrt(2)/2$',r'$0$', r'$squrt(2)/2$',r'$+1$'])
"""上面两行设置刻度,其中前面一个[]中的数字表示刻度的具体值，而后一个[]表示显示出来的刻度值；
两者中，前面的必须是具体到有理数，比如3π/4就不能直接写，而是要写出π/1.33方可以，或者用3*np.pi/4，后面的可以"""

ax = gca()
ax.spines['right'].set_color('none')#设置右边轴线颜色为透明
ax.spines['top'].set_color('none')#设置上边轴线颜色为透明
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
"""----这几行命令是添加轴线(spines)，轴线(spines)是连接刻度标志和标示数据区域边界的线。
它们现在可以被放置在任意地方，它们在子图的边缘。我们将改变这点，因为我们想让它们位于中间。
因为一共有四个轴线(上/下/左/右)。
我们将通过将它们的颜色设置成None，舍弃位于顶部和右部轴线。
然后我们把底部和左部的轴线移动到数据空间坐标中的零点。
------"""


"""---以下一段功能：我们现在使用annotate命令注解一些我们感兴趣的点。
我们选择2π/3作为我们想要注解的正弦和余弦值。
我们将在曲线上做一个标记和一个垂直的虚线。
然后，使用annotate命令来显示一个箭头和一些文本。
----"""
t = 2*np.pi/3
plot([t,t],[0,np.cos(t)], color ='red', linewidth=2.5, linestyle="--")
#画一个垂直的虚线

scatter([t,],[np.cos(t),], 50, color ='red')
#标注这个点，数字 50 表示这点的大小，颜色表示这点的颜色

annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
"""----#标注内容，fontsize=26表示标注文字的大小
xy -- 为点的坐标
xytext -- 为注解内容位置坐标，当该值为None时，注解内容放置在xy处
xycoords and textcoords 是坐标xy与xytext的说明，
若textcoords=None，则默认textNone与xycoords相同，若都未设置，默认为data，
arrowprops -- 用于设置箭头的形状，类型为字典类型
**kwargs -- 用于接收其他设置参数，比如bbox用于设置文本的边框形状----"""

plot([t,t],[0,np.sin(t)], color ='yellow', linewidth=2.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='yellow')
annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(t, np.sin(t)), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


"""-----由于黄色和红色的线，刻度标签现在很难看清。。
我们可以让它们更大并且调整它们的属性使它们的背景半透明。
这将让我们把数据和标签都看清。----"""
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))


show()
