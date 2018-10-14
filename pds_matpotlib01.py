import matplotlib.pyplot as plt
import numpy as np
from pandas import Series
import pandas

#fig = plt.figure()
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax4 = fig.add_subplot(2,2,4)
# #  ax1  ax2  按参数创建两行两列的图 后面则显示的是位置
# #  ax3  ax4

# #画多个图 子图的操作
# fig = plt.figure(figsize = [6,6])  #figsize 指定长和宽的大小
# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)
# #对两个字图分别操作
# ax1.plot(np.random.randint(1,5,5),np.arange(5))
# ax2.plot(np.arange(10)*3,np.arange(10))
# plt.show()

#在同一个图画两条曲线
unrate = pandas.read_csv("UNRATE.csv")

unrate["DATE"] = pandas.to_datetime(unrate["DATE"])
unrate['MONTH'] = unrate['DATE'].dt.month
unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize = (6,3))

plt.plot(unrate[0:12]["MONTH"],unrate[0:12]["VALUE"],c = "red")
plt.plot(unrate[12:24]["MONTH"],unrate[12:24]["VALUE"],c = "blue")

plt.show()