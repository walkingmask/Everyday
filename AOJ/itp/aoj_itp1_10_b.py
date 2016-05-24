# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_B
# 10:13 - 10:20

import math

a, b, C = map(float, raw_input().split())

sinC = math.sin(math.radians(C))
cosC = math.cos(math.radians(C))
c = math.sqrt( a*a + b*b - 2*a*b*cosC )

print ( a * b * sinC ) / 2  # Area
print a + b + c             # Periphery
print b * sinC              # Height

'''
# sankou ni natta kaitou
# 601247 Solution for ITP1_10_B: Triangle by sekibun

import math
a, b, C = map(int, raw_input().split())
S = (a * b * math.sin(math.radians(C))) / 2
c = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(C)))
L = a + b + c
h = (S * 2) / a # great!!
print("%f" % (S, ))
print("%f" % (L, ))
print("%f" % (h, ))
'''