# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_C

import math

def kochCurve(p1, p2, n):
  if n == 0:
    print(p2[0], p2[1])
    return

  v = [(p2[0]-p1[0])/3, (p2[1]-p1[1])/3]
  s = [p1[0]+v[0], p1[1]+v[1]]
  t = [s[0]+v[0], s[1]+v[1]]

  theta = math.atan2(v[1], v[0]) + math.pi/2

  a = math.sqrt((t[0]-s[0])**2+(t[1]-s[1])**2)
  h = 3**(1/2)*a/2
  u = [s[0]+(t[0]-s[0])/2+h*math.cos(theta), s[1]+(t[1]-s[1])/2+h*math.sin(theta)]

  n -= 1
  kochCurve(p1, s, n)
  kochCurve(s, u, n)
  kochCurve(u, t, n)
  kochCurve(t, p2, n)

if __name__ == "__main__":
  n = int(input())
  print(0, 0)
  kochCurve([0, 0], [100, 0], n)
