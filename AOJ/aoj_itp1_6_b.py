# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_B

# input cards list
n = input()
cards = []
for i in range(n):
	cards.append(raw_input().split())

# comp
#marks = ['S', 'H', 'C', 'D']
#for i in marks:
for i in ['S', 'H', 'C', 'D']
	for j in range(1, 14):
		if [i, str(j)] not in cards:
			print i, j