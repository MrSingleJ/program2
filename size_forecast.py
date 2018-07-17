#!python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# CGI处理模块
import sys
import io
import cgi, cgitb 
import patsy
import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn import linear_model
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 
# 获取数据
dist =form.getvalue("name")
val = float(dist)
PATH = "D:\\vscodeproject\\test\\program3\\"
df = pd.read_csv(PATH + 'final.csv')
regr = linear_model.LinearRegression()
y = df.ix[:,["rent"]]
# 拟合
regr.fit(df['size'].reshape(-1, 1), y) 
# 注意此处.reshape(-1, 1)，因为X是一维的！
# 不难得到直线的斜率、截距
a, b = regr.coef_, regr.intercept_
print ("Content-type:text/html\r\n\r\n")
res = str(regr.predict(val)[0])
print("根据面积预测房价："+res)