# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B
# 15:04 - 15:15
# Dictionary

n = input()
dic = set([])
for i in xrange(n):
    order = raw_input().split()
    if order[0][0] == 'i':
        dic.add(order[1])
    else:
        print "yes" if order[1] in dic else "no"