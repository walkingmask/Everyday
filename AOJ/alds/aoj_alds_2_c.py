# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C
# -
# stable sort

def BubbleSort(C, N):
    for i in xrange(0, N):
        for j in reversed(xrange(i+1, N)):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]

def SelectionSort(C, N):
    for i in xrange(N):
        minj = i
        for j in xrange(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]

def isStable(C, N):
    flag = 0
    for i in xrange(1, 14):
        Ct = [C[j] for j in xrange(N) if C[j][1] == str(i)]
        if len(Ct) > 1:
            for k in xrange( len(Ct)-1 ):
                if Ct[k][2] > Ct[k+1][2]:
                    flag = 1
    if flag == 0: print "Stable"
    else:         print "Not stable"

# MAIN
N = input()
C = []
Ct = map(str, raw_input().split())
for i in xrange(N):
    C.append([Ct[i][0], Ct[i][1::], i])

Ct = list(C)
BubbleSort(Ct, N)
print " ".join([Ct[i][0]+Ct[i][1] for i in xrange(N)])
isStable(Ct, N)

Ct = list(C)
SelectionSort(Ct, N)
print " ".join([Ct[i][0]+Ct[i][1] for i in xrange(N)])
isStable(Ct, N)
