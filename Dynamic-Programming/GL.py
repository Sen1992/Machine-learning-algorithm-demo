#-*-coding=UTF-8-*-
#/usr/bin/python
import os
import numpy as np

#读取金矿和人员数据
if os.path.isfile("dataInput.txt"):    
    with open("dataInput.txt",'r') as f:
        data = [map(int,line.split(" ")) for line in f.readlines()]
    #每个金矿需要多少人
    people_need = []
    #每个金矿能产多少黄金
    gold = []
    #总共有多少人数
    people_total = data[0][0]
    #总共有多少金矿
    mine_total = data[0][1]
    for i in range(len(data)-1):
        people_need.append(data[i+1][0])
        gold.append(data[i+1][1])
    #动态规划的核心，记录每种情况的值，使用空间换时间
    max_gold = np.zeros((people_total,mine_total),dtype=int)-np.ones((people_total,mine_total),dtype=int)
    #备忘录
else:
    print "No Input data"
    exit(0) 
