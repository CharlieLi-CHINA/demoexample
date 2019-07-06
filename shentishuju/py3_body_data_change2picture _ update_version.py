# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:07:10 2019

@author: liqilv

python 3
"""
import pandas as pd
import numpy as np
from pylab import *
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter 

def get_excel_data2numpy(path):#将表格数据提取转换成数组
    df = pd.read_excel(path,sheetname=0)#读取
    #print(df.iloc[2:5,:2])#.iloc[行,列]
    #print(df[0:3])#0到3行,0/1/2/3行
    riqi = df.iloc[0:,]#得到所有的数据，每一行是一天的数据
    riqi = np.array(riqi)
    date_time = riqi[:,0]#第一列数据
    sleep_time = riqi[:,1]#第二列数据
    up_time = riqi[:,2]
    sleep = riqi[:,3]
    use_money = riqi[:,4]
    eat_money = riqi[:,5]
    body_state = riqi[:,-1]
    return date_time,sleep_time,up_time,sleep,use_money,eat_money,body_state
def plt_common(date_time=[],data_plt=[],color_plt='red',label_name='dhd',title_file_name='hh',i=0,j=-1):
    #通用画图函数，包含本次输入数组的曲线以及其平均值直线
    #参数依次是日期、要画图的数据、线条颜色、线条标签名称、图的题名、截取数组开始序号、截取数组结尾序号
    i=int(i)#选取的数组开头
    j=int(j)#选取的数组结尾
    zuobiao = date_time[i:j]#确定坐标，以第一列表格中的数据来作为指引
    plt.plot(date_time[i:j],data_plt[i:j],color=color_plt,label=label_name)#画输入数据的曲线
    # markerfacecolor='blue',marker='o'   for语句对应的设定点的样式
    for a, b in zip(zuobiao, data_plt[i:j]):  #标出曲线上数组中的每个点的坐标
        plt.text(a, b, (a,b),ha='center', va='bottom', fontsize=5) 
        
    data_plt_av = [np.mean(data_plt[i:j])]*len(data_plt[i:j])#求平均值
    plt.plot(zuobiao,data_plt_av,color='lightgrey',label=label_name+'_av',linestyle='dashed')#画平均值直线
def plt_sleep_money(date_time=[],sleep_time=[],up_time=[],sleep=[],use_money=[],eat_money=[],begin_number=0,finish_number=-1,title_file_name='hh'):
    #调用 plt_common 模块，画出自己的数据曲线
    #参数值依次是日期、起床节点、睡觉时长、睡觉节点、花销、吃饭花销、截取数组开始序号、截取数组结尾序号、保存的图像文件命名信息
    begin_number=int(begin_number)
    finish_number=int(finish_number)
    
    plt_common(date_time=date_time,data_plt=up_time,color_plt='blue',label_name=title_file_name+'up_time',i=begin_number,j=finish_number)
    plt_common(date_time=date_time,data_plt=sleep,color_plt='green',label_name=title_file_name+'sleep',i=begin_number,j=finish_number)
    plt_common(date_time=date_time,data_plt=sleep_time,color_plt='red',label_name=title_file_name+'sleep_time',i=begin_number,j=finish_number)
    plt.title('body_sleep'+title_file_name)
    plt.legend()
    plt.savefig("{}_body_sleep.png".format(title_file_name), dpi=300)
    plt.figure()
     # 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
    # 指定dpi=200，图片尺寸为 1200*800
    # 指定dpi=300，图片尺寸为 1800*1200
    plt_common(date_time=date_time,data_plt=use_money,color_plt='red',label_name=title_file_name+'use_money',i=begin_number,j=finish_number)
    plt_common(date_time=date_time,data_plt=eat_money,color_plt='yellow',label_name=title_file_name+'eat_money',i=begin_number,j=finish_number)
    plt.title('use_money'+ title_file_name)
    plt.legend()
    plt.savefig("{}_use_money.png".format(title_file_name), dpi=400)
    plt.figure()

if __name__ == "__main__":
    path = "2019up.xlsx"#文件路径
    title_file_name='hh'
    date_time,sleep_time,up_time,sleep,use_money,eat_money,body_state = get_excel_data2numpy(path)#表格数据转换成数组
    plt_sleep_money(date_time,sleep_time,up_time,sleep,use_money,eat_money,0,20,title_file_name)#画自己的数据
    
    plt_common(date_time=date_time,data_plt=body_state,color_plt='brown',label_name='body_state',title_file_name='hh',i=0,j=20)
    plt.title('body_state'+ title_file_name)
    plt.legend()
    plt.savefig("{}_body_state.png".format(title_file_name), dpi=400)
    plt.figure()
