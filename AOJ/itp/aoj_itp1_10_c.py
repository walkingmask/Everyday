# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C
# 10:13 - 10:20

import math

while 1:

    # input the students number
    n = input()
    if n == 0:
        break
    # input the points
    s = map(float, raw_input().split())
    # get the average of points
    ave = 0
    for i in s:
        ave += i
    ave = ave / len(s)
    # get the standard deviation
    alpha = 0
    for i in s:
        alpha += (i - ave)*(i - ave)
    alpha = math.sqrt( alpha/len(s) )
    # print
    print alpha

'''
sankou ni natta kaitou
#1530377 Solution for ITP1_10_C: Standard Deviation by uyuyu

import math
while True:
    n=input()
    if n==0: break
    s=map(int,raw_input().split())
    mean=float(sum(s))/len(s)
    var=[(x-mean)**2/n for x in s]
    print math.sqrt(sum(var))
'''