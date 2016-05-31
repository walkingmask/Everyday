# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
# 07:51 - 08:39
# ref http://d.hatena.ne.jp/pashango_p/20090704/1246692091

def isPrime(num):
    if num == 2: return 1
    if num < 2 or num&1 == 0: return 0
    if pow(2, num-1, num) == 1: return 1
    return 0

n = input()
s = 0
for i in xrange(n):
    s += isPrime(input())

print s

'''
sankou ni natta code
#899004 Solution for ALDS1_1_C: Prime Numbers by roiti
return no kakikata ga omoshiroi

def isPrime(p):
    if p == 2: return 1
    if p < 2 or p&1 == 0: return 0
    return 1 if pow(2,p-1,p) == 1 else 0
     
n = int(raw_input())
print sum(isPrime(int(raw_input())) for i in range(n))
'''