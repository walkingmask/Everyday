# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D
# -
# bakada

n = input()
R = [input() for i in xrange(n)]

Rmin = n
maxdif = R[1] - R[0]

while Rmin > 0:
    tRmin = R.index(min(R[0:Rmin]))
    Rmax = R.index(max(R[tRmin:Rmin]))
    print tRmin, R[tRmin]
    print Rmax, R[Rmax]
    if tRmin == Rmax:
        if tRmin == n-1:
            tRmin-=1
        elif tRmin < n-1:
            Rmax = tRmin + 1
    Rmin = tRmin
    if (R[Rmax] - R[Rmin]) > maxdif:
        maxdif = R[Rmax] - R[Rmin]

print maxdif

'''
sugoi kaitou
#1430728 Solution for ALDS1_1_D: Maximum Profit by zyunpe

import sys
 
n = input()
minv = input()
maxv = - 1000000000
nums = map(int, sys.stdin.readlines())
for num in nums:
    maxv = num - minv if num - minv > maxv else maxv
    minv = num if num < minv else minv

print maxv

note
Rmax = (Rt-Rmin > Rmax)? Rt-Rmin : Rmax;
Rmin = (Rt < Rmin)? Rt : Rmin;
'''