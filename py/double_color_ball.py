# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 23:57:46 2018

@author: zhengjt
"""


import json
import urllib3

#利用urllib2获取网络数据
http = urllib3.PoolManager()
#url ="http://f.apiplus.net/ssq.json"     
url ="http://caipiaojieguo.com/api/lottrey?biaoshi=ssq&format=json&rows=10" 
r = http.request('GET', url)
value=json.loads(r.data)
rootlist=value.keys()
for rootkey in rootlist:
    print(rootkey)
datas=value['data']

num=len(datas)
i=0
#逐个号码解析出来

#while(i<num):
#    str_code=datas[i]['opencode']
#    blue_ball=str_code[-2:]
#    print('blue ball: ',blue_ball)
#    str_code_split=str_code[:-3].split(',')
#    j=0
#    while(j<len(str_code_split)):
#        print(datas[i]['expect'],str_code_split[j])
#        j=j+1
#    i=i+1
    
#检索是否中奖
targe_red_ball=['13', '03', '14', '16', '25', '28']
while(i<num):
#    from彩票结果网
    str_code=datas[i]['result']
    blue_ball=str_code[-2:]
    print('blue ball: ',blue_ball)
    red_ball_list=str_code[:-3].split(',')
#    开彩网
#    str_code=datas[i]['opencode']
#    blue_ball=str_code[-2:]
#    print('blue ball: ',blue_ball)
#    red_ball_list=str_code[:-3].split(',')
#    向字典加入内容项
    datas[i]['blue_ball']=blue_ball
    datas[i]['red_ball']=red_ball_list
#    print(datas[i]['expect']+':',red_ball_list)
    print(datas[i]['qishu']+':',red_ball_list)
    j=0
    result=[0,0,0,0,0,0]
    while(j<len(red_ball_list)):
        result[j]=red_ball_list.count(targe_red_ball[j])
        j+=1
    print('中奖结果：',result)
    i+=1
    
#把字典写到文件    
jsObj = json.dumps(datas)
 
fileObject = open('double_color_ball.json', 'w')
fileObject.write(jsObj)
fileObject.close()
    