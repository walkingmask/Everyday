# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_D

import numpy as np
import sys

n, m, l = map(int, raw_input().split())
a = []
b = []
for i in range(n):
	a.append(map(int, raw_input().split()))
for i in range(m):
	b.append(map(int, raw_input().split()))

a = np.matrix(a)
b = np.matrix(b)

c = a * b

for i in xrange(n):
	for j in xrange(l-1):
		sys.stdout.write(str(c[i,j])+" ")
	print c[i,l-1]