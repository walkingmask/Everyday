# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B
# referenced: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=1515450#1

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
  for k in range(left, right):
    count += 1
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1

def mergeSort(A, left, right):
  if left + 1 < right:
    mid = int((left + right)/2)
    mergeSort(A, left, mid)
    mergeSort(A, mid, right)
    merge(A, left, mid, right)

if __name__ == "__main__":
  n = int(input())
  S = list(map(int, input().split()))
  mergeSort(S, 0, len(S))
  print(" ".join(map(str, S)))
  print(count)
