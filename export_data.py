#!python
#-*- coding:utf-8 -*-
import pymysql
import sys
import io
import csv
import codecs
import pandas as pd
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def query_all(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()
with open('D:\\vscodeproject\\test\\program3\\lianjia.csv', mode='w', encoding='utf-8') as f:
    write = csv.writer(f, dialect='excel')
    db = pymysql.connect('localhost','root','root','lianjia',charset='utf8')
    cur = db.cursor()
    sql = 'select * from lianjia'
    results = query_all(cur=cur, sql=sql, args=None)
    for result in results:
        write.writerow(result)
print ("Content-type:text/html\r\n\r\n")