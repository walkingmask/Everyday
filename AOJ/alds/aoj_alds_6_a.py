# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_A

def CountingSort(A, n, B, k):
  C = [0]*(k+1)

  for i in range(n):
    C[A[i]] += 1

  for i in range(1, k+1):
    C[i] = C[i] + C[i-1]

  for i in reversed(range(n)):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= 1

def main():
  n = int(input())
  A = list(map(int, input().split()))
  B = [0]*n
  CountingSort(A, n, B, max(A))
  print(" ".join(map(str, B)))

if __name__ == "__main__":
  main()
