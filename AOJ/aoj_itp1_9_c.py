# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_C

n = input()

tp = hp = 0

for i in xrange(n):

    tc, hc = map(str, raw_input().split())

    if   tc > hc:
        tp+=3
    elif tc < hc:
        hp+=3
    else:
        tp+=1
        hp+=1

print tp, hp
