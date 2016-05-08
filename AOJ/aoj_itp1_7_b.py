# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B

while 1:

	n, x = map(int, raw_input().split())
	if n == 0 and x == 0:
		break

	count = 0
	for i in xrange(1, n-1):
		for j in xrange(i+1, n):
			for k in xrange(j+1, n+1):
				if i+j+k > x:
					break
				if i+j+k == x:
					count += 1
	print count