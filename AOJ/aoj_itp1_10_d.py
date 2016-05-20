# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_D
# 10:30 - 10:56

import math

n = input()
x = map(float, raw_input().split())
y = map(float, raw_input().split())
temp = p1 = p2 = p3 = pinf = 0

for i,j in zip(x, y):
    temp = math.fabs(i - j)
    p1 += temp
    p2 += temp ** 2
    p3 += temp ** 3
    if temp > pinf:
        pinf = temp

print u"%f\n%f\n%f\n%f" % (p1, p2**(1.0/2), p3**(1.0/3), pinf)