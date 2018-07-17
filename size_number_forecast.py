#!python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# CGI处理模块
import os
import io
import sys
import cgi, cgitb 
import pandas as pd
import requests
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 
# 获取数据
dist =3#form.getvalue("name")
num =3#form.getvalue("num")
number = float(num)
area = float(dist)
PATH = "D:\\vscodeproject\\test\\program3\\"
df = pd.read_csv(PATH + 'final.csv')
X = df.ix[:,[ "size","type"]]
y = df.ix[:,["rent"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
regr = linear_model.LinearRegression()
regr.fit(X_train,y_train)
data = [[area,number]]
columns=["size","type"]
X_test2 = pd.DataFrame(data=data,columns=columns)
y_pred = regr.predict(X_test2)
print ("Content-type:text/html\r\n\r\n")
y_pred2 = str(y_pred[0])
print("根据住房面积和房间数量预测房价："+ y_pred2)
