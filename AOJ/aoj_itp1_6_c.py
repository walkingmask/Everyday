# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_B

import sys

buildings = [[[0 for i in xrange(10)] for j in xrange(3)] for k in xrange(4)]

n = input()

for i in xrange(n):
	b, f, r, v = map(int, raw_input().split())
	buildings[b-1][f-1][r-1] += v

for i in xrange(4):
	if i != 0:
		print "####################"
	for j in xrange(3):
		for k in xrange(10):
			sys.stdout.write(" "+str(buildings[i][j][k]))
		print