# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import pandas as pd
def readFromExcle():
    df = pd.read_excel('D:\bianyingE\guolab\paper\2')



'''
一、基础绘图
1. 定义xy坐标
2. 使用plot绘制xy坐标
3. 显示图形
'''
def print_simple():
    x=[1,2,3,4]
    y=[1,4,9,16]
    plt.plot(x,y)
    plt.show()

'''
二、定义绘图属性
1. color：线条颜色，值r表示红色（red）
2. marker：点的形状，值o表示点为圆圈标记（circle marker）
3. linestyle：线条的形状，值dashed表示用虚线连接各点

https://www.cnblogs.com/big-big-watermelon/p/14052165.html

plt.plot(x, y, color='r',marker='o',linestyle='dashed')
'''
def print_simple_1():
    x=[1,2,3,4]
    y=[1,4,9,16]
    plt.plot(x,y,color='r',marker='o',linestyle='dashed')
    plt.show()

'''
三、添加注释标题
1. 添加文本 
x轴文本 plt.xlabel('x坐标轴')
y轴文本 plt.ylabel('y坐标轴')
标题 plt.title('标题')

2. 坐标轴刻度设置
1)刻度范围
plt.xticks(np.arange(-5, 5, 0.5),fontproperties = 'Times New Roman', size = 10)
plt.yticks(np.arange(-2, 2, 0.3),fontproperties = 'Times New Roman', size = 10)

ps:
plt.xlabel('$m^2$  CO$_2$')   #此处表示下标  '$\it{r}$$_1$'
plt.ylabel('$\it{AAA}$$_1$')  #斜体+上标
#上标用^，下标用_

2)刻度方向
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

3. 坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-2, 2))

4. 坐标轴名称/标题细节
plt.xlabel('xxxxxxxxxxx',fontdict={'family' : 'Times New Roman', 'size' : 16})
1) labelpad=5 标题距离刻度线范围


5.图例
plt.legend(prop={'family' : 'Times New Roman', 'size' : 16})

'''
def print_simple_2():
    x=[1,2,3,4]
    y=[1,4,9,16]
    y2=[1,2,3,4]
    l1,  = plt.plot(x,y,color='r',marker='o',linestyle='solid')
    l2,  = plt.plot(x, y2, color='b', marker='^', linestyle='dashed')
    plt.xlabel('xxxx', fontdict={'family' : 'Times New Roman','size' : 16})
    plt.ylabel('yyyy', fontdict={'family' : 'Times New Roman','size' : 16})
    plt.title('test', fontdict={'family' : 'Times New Roman','size' : 18})
    plt.xticks(np.arange(0, 5, 1), fontproperties='Times New Roman', size=16)
    plt.yticks(np.arange(0, 16, 1), fontproperties='Times New Roman', size=16)
    plt.legend(handles=[l1,l2], labels=['l1','l2'],prop={'family' : 'Times New Roman', 'size' : 16}, loc='best')
    plt.show()

'''
四、图片大小，边框
1. 设置背景图
fig=plt.figure(figsize=(10,6))
fig.patch.set_facecolor('white')#设置背景颜色
fig.patch.set_alpha(1)#设置透明度

2. 设置边框
1) 边框宽度、有无
bwith = 1 #边框宽度设置为2
ax = plt.gca()#获取边框
#设置边框
ax.spines['bottom'].set_linewidth(bwith)#图框下边
ax.spines['left'].set_linewidth(bwith)#图框左边
ax.spines['top'].set_linewidth(bwith)#图框上边
ax.spines['right'].set_linewidth(bwith)#图框右边
#取消边框
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

2) 网格线
plt.grid() #显示网格线


3. 坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-2, 2))

4. 坐标轴间距


5. 坐标轴名称/标题细节
plt.xlabel('xxxxxxxxxxx',fontdict={'family' : 'Times New Roman', 'size' : 16})
1) labelpad=5 标题距离刻度线范围


6. 图例
plt.legend(prop={'family' : 'Times New Roman', 'size' : 16})



others
  fig.tight_layout()#调整整体空白
  plt.subplots_adjust(wspace =0, hspace =0)#调整子图间距

'''
def print_simple_2():
    x=[1,2,3,4]
    y=[1,4,9,16]
    y2=[1,2,3,4]
    l1,  = plt.plot(x,y,color='r',marker='o',linestyle='solid')
    l2,  = plt.plot(x, y2, color='b', marker='^', linestyle='dashed')
    plt.xlabel('xxxx', fontdict={'family' : 'Times New Roman','size' : 16})
    plt.ylabel('yyyy', fontdict={'family' : 'Times New Roman','size' : 16})
    plt.title('test', fontdict={'family' : 'Times New Roman','size' : 18})
    plt.xticks(np.arange(0, 5, 1), fontproperties='Times New Roman', size=16)
    plt.yticks(np.arange(0, 16, 1), fontproperties='Times New Roman', size=16)
    plt.legend(handles=[l1,l2], labels=['l1','l2'],prop={'family' : 'Times New Roman', 'size' : 16}, loc='best')
    plt.show()

'''
五、绘制柱形图
1. 



'''
def print_simple_3():
    x=[1,2,3,4]
    y=[1,4,9,16]
    plt.plot(x,y,color='r',marker='o',linestyle='dashed')
    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_simple()
    print_simple_1()
    print_simple_2()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
