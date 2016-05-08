# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_D

matrix = []
vector = []

n, m = map(int, raw_input().split())

for i in xrange(n):
	matrix.append(map(int, raw_input().split()))

for i in xrange(m):
	vector.append(input())

for i in xrange(n):
	ans = 0
	for j in xrange(m):
		ans += matrix[i][j] * vector[j]
	print ans