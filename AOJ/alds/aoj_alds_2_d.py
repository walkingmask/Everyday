# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_D
# -
# shell sort
# bimyou

def insertionSort(A, n, g):
    cnt = 0
    for i in xrange(g, n):
        v = A[i]
        j = i - g
        while (j >= 0) and (A[j] > v):
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return cnt

def shellSort(A, n):
    # variables
    cnt, m, t = 0, 1, n
    # getting m
    while (t-1)/3 > 0:
        t, m = (t-1)/3, m+1
    print m
    # creating and printing G
    G = [1]
    for i in xrange(1,m):
        G.append(1+G[i-1]*3)
    G = list(reversed(G))
    print " ".join( map(str, G) )
    # sorting
    for i in xrange(0, m):
        cnt += insertionSort(A, n, G[i])
    return cnt

# MAIN
n = input()
A = [input() for i in xrange(n)]
cnt = shellSort(A, n)
print cnt
for i in xrange(n):
    print A[i]
