#!python
#-*- coding:utf-8 -*-
import io
import os
import sys
import requests
import re
import random
#import MySQLdb
import pymysql
from bs4 import BeautifulSoup
class house():
    def get_house(self):
        num = 0
        quyu = ['furong','tianxin','kaifu','yuelu','yuhua']
        user_agent=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        ]
        headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': user_agent[random.randint(0,5)]
        }
        #db = MySQLdb.connect('localhost','root','root','lianjia',charset='utf8')
        db = pymysql.connect('localhost','root','root','lianjia',charset='utf8')
        cursor = db.cursor()
        sql =  "truncate table lianjia"
        cursor.execute(sql)
        for dist in quyu:
            url1 = 'http://cs.lianjia.com/zufang/%s/pg' %dist
   
            for i in range(1,3):
                url = url1+str(i)+'/'     
                r = requests.get(url,headers=headers)
                r.encoding = 'utf8'
                html = r.text
            #PATH = "e:\\python3\\"
            #with open(PATH + "lianjia.html","a",encoding='utf-8') as f:
            #    f.write(html)   
                soup = BeautifulSoup(html)  
                for tag in soup.find('ul',id='house-lst').find_all('div',class_='info-panel'):
                    ss = []
                    for aa in tag.find_all('a'):
                        ss.append(aa.string)              
                    for bb in tag.find_all('span'):
                        ss.append(bb.string)
                    #ss.append(dist)
                    if len(ss) == 15:
                        sql = "insert into lianjia(title,village,are,type,size,ori,info,rent,people,dist) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(ss[0],ss[1],ss[2],ss[4],ss[6],ss[7],ss[11],ss[13],ss[14],dist)
                        all_info = (u'" %s", " %s", " %s", " %s", "%s", " %s", "%s", "%s"," %s","%s"\n' %
    (ss[0],ss[1],ss[2],ss[4],ss[6],ss[7],ss[11],ss[13],ss[14],dist))
                        data.append(all_info)
                        num += 1                                        
                    elif len(ss) == 18:
                        sql = "insert into lianjia(title,village,are,type,size,ori,info,rent,people,dist) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(ss[0],ss[1],ss[2],ss[4],ss[6],ss[7],ss[11],ss[16],ss[17],dist)
                        all_info = (u'" %s", " %s", " %s", " %s", "%s", " %s", "%s", "%s"," %s","%s"\n' %
    (ss[0],ss[1],ss[2],ss[4],ss[6],ss[7],ss[11],ss[13],ss[14],dist))
                        num +=1 
                    else:
                        continue
                    cursor.execute(sql) 
        return num                            
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
data = []
test = house()
num = str(test.get_house())
print ("Content-type:text/html\r\n\r\n")
print("总共采集到数据"+num+"条")


