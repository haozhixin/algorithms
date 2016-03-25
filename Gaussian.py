#!/usr/bin/python
#-*- coding:utf-8 -*-
#算出1~100的和,普通方法和高斯算法比较

#普通方法
num = 0
for i in range(0,100):
	num +=(i+1)
print num

#高斯算法
num = 1
end = 100
print (num+end)*end/2
