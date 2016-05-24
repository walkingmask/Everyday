# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_D

import sys

N, M, L = map(int, raw_input().split())
a = []
b = []
for n in range(N):
	a.append(map(int, raw_input().split()))
for m in range(M):
	b.append(map(int, raw_input().split()))

c = [[0 for l in xrange(L)] for n in xrange(N)]

for n in xrange(N):
	for l in xrange(L):
		for m in xrange(M):
			c[n][l] += a[n][m] * b[m][l]

for n in xrange(N):
	for l in xrange(L-1):
		sys.stdout.write(str(c[n][l])+" ")
	print c[n][L-1]