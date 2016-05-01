# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_A

import sys

while 1:
	h, w = map(int, raw_input().split())
	if h == 0 & w == 0:
		break
	else:
		for i in xrange(h):
			for j in xrange(w):
				sys.stdout.write("#")
			print ""
	print ""

