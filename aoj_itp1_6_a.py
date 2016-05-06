# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_D

import sys

n = input()
ai = raw_input()
ai = map(int, ai.split())

for i in reversed(range(1, n)):
	sys.stdout.write(str(ai[i])+" ")
print ai[0]