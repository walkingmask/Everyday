# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A
# -

n = input()
S = raw_input().split()
q = input()
T = raw_input().split()

s = 0
for i in T:
    if i in S:
        s+=1
print s

'''
sankou ni natta kaitou using set
#673163 Solution for ALDS1_4_A: Linear Search by utisam

n = input()
S = set([int(s) for s in raw_input().split()])
m = input()
T = set([int(s) for s in raw_input().split()])
print len(T & S)
'''