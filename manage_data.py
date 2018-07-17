#!python
#-*- coding:utf-8 -*-
import pymysql
import sys
import io
import csv
import codecs
import pandas as pd
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def parse_info2(row):
       beds = row.strip().split('室')[0]
       rooms_temp = row.strip().split('室')[1]
       rooms = rooms_temp.strip().split('厅')[0]
       return int(beds) + int(rooms)
def parse_info(row):
       return row.strip().split('平米')[0]
CSV_PATH = r"D:\\vscodeproject\\test\\program3\\lianjia.csv"
df=pd.read_csv(CSV_PATH,names=['title','village','are','type','size','ori','info','rent','people','dist'])
sudf = df[['type','size','rent','dist']]
X = sudf.ix[:,[ "size","type"]]
sudf.loc[:,'rent'] = df['rent'].astype(int)
y = sudf.ix[:,["rent"]]
X['size'] = X['size'].apply(parse_info)
X['type'] = X['type'].apply(parse_info2)
sudf['size'] = X['size']
sudf['type'] = X['type']
sudf.to_csv('d:\\vscodeproject\\test\\final.csv', header=True, index=True)
print ("Content-type:text/html\r\n\r\n")





