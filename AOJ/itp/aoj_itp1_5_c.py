# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_C

import sys

while 1:
	h, w = map(int, raw_input().split())
	if h == 0 and w == 0:
		break
	else:
		for i in xrange(h):
			if (i%2) == 0:
				for j in xrange(w):
					if (j%2) == 0:
						sys.stdout.write("#")
					else:
						sys.stdout.write(".")
				print ""
			else:
				for j in xrange(w):
					if (j%2) == 0:
						sys.stdout.write(".")
					else:
						sys.stdout.write("#")
				print ""
	print ""

