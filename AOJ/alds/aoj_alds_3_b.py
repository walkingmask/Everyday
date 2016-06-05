# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A
# -
# Round-Robin scheduling with queue

# input
n, q = map(int, raw_input().split())
procs = [raw_input().split() for i in xrange(n)]
procs = list(reversed(procs))

# procsessing
cnt, lack = 0, 1
while lack > 0:
    lack = 0
    tprocs = []
    for i in xrange(n):
        proc = procs.pop()
        t = int(proc[1])
        if t <= q:
            cnt += t
            print proc[0], cnt
            n -= 1
        else: # t > q
            cnt += q
            t = t - q
            lack += t
            proc[1] = str(t)
            tprocs.append(proc)
    procs = list(reversed(tprocs))