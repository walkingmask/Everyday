# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_B

import sys

while 1:
	h, w = map(int, raw_input().split())
	if h == 0 and w == 0:
		break
	else:
		for i in xrange(h):
			if i == 0 or i == (h-1):
				for j in xrange(w):
					sys.stdout.write("#")
				print ""
			else:
				sys.stdout.write("#")
				for j in xrange(w-2):
					sys.stdout.write(".")
				print "#"
	print ""

