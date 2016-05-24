# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_D

n = int(raw_input())
cout = ""

for i in range(1,n+1):
	x = i

	if (x%3) == 0:
		cout = cout + " " + str(i)
		continue

	while x > 0:
		if (x%10) == 3:
			cout = cout + " " + str(i)
			break
		x /= 10

print cout
