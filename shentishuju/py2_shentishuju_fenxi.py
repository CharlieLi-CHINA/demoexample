# -*- coding: utf-8 -*-
"""
Created on Sun Sep 03 10:10:21 2017

导入自己的表格数据进行绘图分析
@author: liqilv
"""
from pylab import *
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook
import numpy as np 

wan_data=[]
zao_data=[]
shijian_data=[]
x_volte=[]
temp=[]
wb = open_workbook('20160801-20170731_body_data.xlsx')
for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        print 'the row is:',row
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print values
        wan_data.append(values[0])
        zao_data.append(values[1])
        shijian_data.append(values[1]-values[0])
#from xlsx import data
"""------通过以上代码，使得xlsx表格数据被提取到x_data与y_data俩个列表上，x、y分别
对应表格中第一和第二列的数据，如果还有第三、四，那就再增加个表格来提取-----"""        


figure(figsize=(10,2),dpi=100)

plt.subplot(312)          
#plt.plot(wan_data, color="blue",linewidth=2,linestyle="-",label="sleep time")
daydate=range(0,len(wan_data))
plt.bar(daydate,wan_data,color='b',width = .5,alpha=0.6,label="sleep time")
legend(loc='upper right')
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
xticks( [0,30, 60, 91,121, 152, 183,211, 242,272,303,333,364],
       [r'$0801$',  r'$0901$',r'$1001$',r'$1101$',  r'$1201$',r'$0101$',r'$0201$', 
        r'$0301$', r'$0401$',r'$0501$',  r'$0601$',r'$0701$',r'$0801$'])



    
plt.subplot(311)  
#plt.plot(zao_data, color="red",label="getup time")
daydate=range(0,len(zao_data))
plt.bar(daydate,zao_data,color='r',width = .5,alpha=0.6,label="getup time")
legend(loc='upper right')
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
xticks( [0,30, 60, 91,121, 152, 183,211, 242,272,303,333,364],
       [r'$0801$',  r'$0901$',r'$1001$',r'$1101$',  r'$1201$',r'$0101$',r'$0201$', 
        r'$0301$', r'$0401$',r'$0501$',  r'$0601$',r'$0701$',r'$0801$'])
yticks([5,6, 7,8, 9,10,11],[r'$5am$', r'$6am$',r'$7am$',r'$8am$',r'$9am$',r'$10am$',r'$11am$'])
#yticks(5,12,0.5,[r'$5am$', r'$6am$',r'$7am$',r'$7:30am$',r'$8am$',r'$8:30am$',r'$9am$',r'$10am$',r'$11am$'])


plt.subplot(313) 
plt.plot(shijian_data, color="yellow",label="shuimin time")
legend(loc='upper right')
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
xticks( [0,30, 60, 91,121, 152, 183,211, 242,272,303,333,364],
       [r'$0801$',  r'$0901$',r'$1001$',r'$1101$',  r'$1201$',r'$0101$',r'$0201$', 
        r'$0301$', r'$0401$',r'$0501$',  r'$0601$',r'$0701$',r'$0801$'])  
"""---
plt.title(u"20160801-20170731_sleep time")
plt.legend()
plt.xlabel(u"input-deg")


plt.title(u"20160801-20170731_getup time")
plt.legend()

plt.ylabel(u"output-V")

---"""


plt.show()
print 'over!'