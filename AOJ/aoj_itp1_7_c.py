# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_C

import sys

r, c = map(int, raw_input().split())

c_sum = 0
sum_vector = [0 for i in xrange(c+1)]

for i in xrange(r):
	temp = map(int, raw_input().split())
	temp.append(sum(temp))
	for j in xrange(c):
		sum_vector[j] += temp[j]
		sys.stdout.write(str(temp[j])+" ")
	else:
		sum_vector[c] += temp[c]
		print temp[c]

for i in xrange(c):
	sys.stdout.write(str(sum_vector[i])+" ")
print sum_vector[c]