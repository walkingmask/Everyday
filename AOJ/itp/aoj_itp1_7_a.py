# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_A

m, f, r = map(int, raw_input().split())

while m != -1 or f != -1 or r != -1:

	s = m + f

	if m == -1 or f == -1:
		print "F"
	elif s >= 80:
		print "A"
	elif s >= 65:
		print "B"
	elif s >= 50:
		print "C"
	elif s >=30:
		if r >= 50:
			print "C"
		else:
			print "D"
	else:
		print "F"

	m, f, r = map(int, raw_input().split())