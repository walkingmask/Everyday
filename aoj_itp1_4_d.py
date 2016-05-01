# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_D

n = input()
ai = raw_input()
ai = map(int, ai.split())

print min(ai), max(ai), sum(ai)