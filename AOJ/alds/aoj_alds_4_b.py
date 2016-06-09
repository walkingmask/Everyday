# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B
# 10:10 - 10:20
# Binary Search

n = input()
S = set(raw_input().split())
q = input()
T = set(raw_input().split())

print len(T&S)