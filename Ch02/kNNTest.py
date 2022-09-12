'''
Created on Oct 27, 2010

@author: Peter
'''
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

import kNN

fig = plt.figure()
ax = fig.add_subplot(311)
datingDataMat,datingLabels = kNN.file2matrix('./Ch02/datingTestSet.txt')
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
ax.axis([-2,25,-0.2,2.0])
plt.xlabel('玩游戏所耗时间百分比')
plt.ylabel('每周消费冰淇淋公升数')

ax = fig.add_subplot(312)
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.xlabel('每年获取的飞行常客里程数')
plt.ylabel('玩游戏所耗时间百分比')

ax = fig.add_subplot(313)
ax.scatter(datingDataMat[:,0], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.xlabel('每年获取的飞行常客里程数')
plt.ylabel('每周消费冰淇淋公升数')


plt.show()

#Test dating class
# kNN.datingClassTest()
