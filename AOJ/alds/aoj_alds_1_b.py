# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B
# 06:20 - 06:26

def euclideanAlgorithm(x, y):
    if y == 0: return x
    return euclideanAlgorithm(y, x%y)

# MAIN
x, y = map(int, raw_input().split())
print euclideanAlgorithm(x, y)