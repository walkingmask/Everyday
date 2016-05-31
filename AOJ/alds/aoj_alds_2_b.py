# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B
# 06:45 - 06:56
# selection sort

def selectionSort(A, N):
    count = 0
    for i in xrange(N):
        minj = i
        cflag = 0
        for j in xrange(i, N):
            if A[j] < A[minj]:
                minj = j
                cflag = 1
        A[i], A[minj] = A[minj], A[i]
        count+=cflag
    return count

# MAIN
N = input()
A = map(int, raw_input().split())
c = selectionSort(A, N)
print " ".join(map(str, A))
print c

'''
wasuretara dame
print " ".join(map(str, A))
(from #1513747 Solution for ALDS1_2_A: Bubble Sort by shinkanouchi)
'''