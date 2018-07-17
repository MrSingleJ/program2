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
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 
# 获取数据
dist =form.getvalue("name")
#dist2 = str(dist)
PATH = "D:\\vscodeproject\\test\\program3\\"
df = pd.read_csv(PATH + 'final.csv')
f = 'rent ~ dist'
y, X = patsy.dmatrices(f, df, return_type='dataframe')
results = sm.OLS(y, X).fit()
to_pred_idx = X.iloc[0].index
to_pred_zeros = np.zeros(len(to_pred_idx))
tpdf = pd.DataFrame(to_pred_zeros, index=to_pred_idx, columns=['value'])
tpdf['value'] = 0
tpdf.loc['Intercept'] = 1
#tpdf.loc['Beds'] = 2
str1='dist[T.'+dist+']'
tpdf.loc[str1] = 1
pred = results.predict(tpdf['value'])
print ("Content-type:text/html\r\n\r\n")
re = str(pred[0])
print("预测"+dist+"房价为:"+re)

