# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D
# awesome answer: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=2222957#1

# // (slash slash operator)
# int(10/3) == 10//3

count = 0

def merge(A, left, mid, right):
  global count
  n1 = mid - left
  n2 = right - mid
  L = A[left:left+n1]
  R = A[mid:mid+n2]
  L.append(float("inf"))
  R.append(float("inf"))
  i = 0
  j = 0
  numLeft = len(L)-1 # the number of L's elements
  for k in range(left, right):
    if R[j] < L[i]:
      A[k] = R[j]
      j += 1
      count += numLeft-i # the number of inversions to R[j]
    else:
      A[k] = L[i]
      i += 1

def mergeSort(A, left, right):
  if left + 1 < right:
    mid = (left + right)//2
    mergeSort(A, left, mid)
    mergeSort(A, mid, right)
    merge(A, left, mid, right)


def main():
  n = int(input())
  A = list(map(int, input().split()))
  mergeSort(A, 0, n)
  print(count)

if __name__ == "__main__":
  main()
