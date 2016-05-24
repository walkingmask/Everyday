# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A
# -

def insertionSort(A, N):
    for i in xrange(1, N):
        printList(A, N)
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j-=1
        A[j+1] = v
    return A

def printList(A, N):
    for i in xrange(N):
        print A[i],
    print

# MAIN
N = input()
A = map(int, raw_input().split())

A = insertionSort(A, N)
printList(A, N)

'''
omoshiroi kaito -> print method
#1536466 Solution for ALDS1_1_A: Insertion Sort by kuwatoro

N = input()
A = map(int, raw_input().split())
for i in range(len(A)):
    v = A[i]
    j = i - 1
    while (j >= 0) & (A[j] > v):
        A[j+1] = A[j]
        j -= 1
    A[j+1] = v
    print ' '.join(map(str, A))
'''