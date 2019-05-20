# coding=utf-8
# http://blog.csdn.net/piaoxuezhong/article/details/54619824
# 简单绘图matplotlib.pyplot

# 1,使用plot()函数画图
# import  matplotlib.pyplot as plt
# plt.plot([1,2,3,4])      #matplotlib假设它是y轴的数值序列,自动生成x轴的值【0,3】
# plt.ylabel('numbers')    #给y轴加注释
# plt.show()

# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4],[1,8,27,64], 'ro')
# plt.axis([0,5,0,70])     #axis([xmin,xmax,ymin,ymax]),给出了坐标轴的范围。
# plt.show()

# 2,线的属性
# import numpy as np
# import matplotlib.pyplot as plt
# f = np.arange(0,5,0.1)    #x轴从0到5,间隔0.1
# # red dashes-破折号, blue squares and green triangles-三角形
# plt.plot(f,f,'r--',f,f**2,'bs',f,f**3,'g^')
# plt.show()

# 3,多个图像
# import numpy as np
# import matplotlib.pyplot as plt
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# t1 = np.arange(0.0, 5.0, 0.04)
# t2 = np.arange(0.0, 5.0, 0.02)
# plt.figure(1)
# plt.subplot(211)      #2*1--第1个
# plt.plot(t1,f(t1),'bo',  t2,f(t2),'k')  #'bo'是圆, 'k'是线性
# plt.subplot(212)      #2*1--第2个
# plt.plot(t2,np.cos(2*np.pi*t2),'r--')
# plt.show()

# #为图像做文本说明 pylab
# import numpy as np
# import pylab as pl
#
# data = np.random.normal(0,2,100)
# #做直方图
# pl.hist(data)
#
# pl.xlabel('distribute')
# pl.ylabel('Probability')
# pl.title('Histogram')
# pl.text(0,40,r'$\mu=0,\ \sigma=2$')
# pl.axis([-10,10,0,50])
# #网格
# pl.show()

# #动态图-正弦波
# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation
#
# fig = plt.figure()
# ax = plt.axes(xlim=(0,2), ylim=(-2,2))
# line, = ax.plot([],[],lw=2)
# # 绘制每一帧的背景
# def init():
#     line.set_data([],[])
#     return line,
# # i是帧号
# def animate(i):
#     x = np.linspace(0,2,1000)
#     y = np.sin(2*np.pi*(x - 0.01*i))
#     line.set_data(x,y)
#     return line,
# #
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)
# plt.show()

#python变成从入门到实践
# Scatter绘制一系列点-P292
# import matplotlib.pyplot as Jone
#
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
#
# Jone.scatter(x_values, y_values, c='red', edgecolor='none', s=100)
# # Jone.plot(x_values, y_values, linewidth=3)
# Jone.show()

#for循环,颜色渐变
# import matplotlib.pyplot as Jone
# x_values = list(range(1,1001))
# y_values = [x**2 for x in x_values]        # x**2表示x的平方
# Jone.scatter(x_values, y_values, c=y_values, cmap=Jone.cm.Blues, edgecolor='none' ,s=30)
# Jone.axis([0,1100, 0,1100000])
# # Jone.show()
# Jone.savefig('circle.png',bbox_inches='tight')   #保存图片并且剪切图片空白区域

#http://blog.csdn.net/pipisorry/article/details/40005163
# 散点图、梯形图、柱状图、填充图,柱状图bar()
# import numpy as np
# import matplotlib.pyplot as plt
#
# n = np.array([0,1,2,3,4,5])
# x = np.linspace(-0.75, 1. ,100)
#
# fig, axes = plt.subplots(1, 4, figsize=(12, 3))
#
# axes[0].scatter(x, x+0.25*np.random.randn(len(x)))
# axes[1].step(n, n**2, lw=2)
# axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)     #柱状图
# axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)  #填充图
# plt.show()






