# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_A
# 10:13 - 10:20

import math

x1, y1, x2, y2 = map(float, raw_input().split())

print math.sqrt( ((x1-x2) * (x1-x2)) + ((y1-y2) * (y1-y2)) )