# input
a, b = map(int, raw_input().split())

# calc
d = a // b
r = a % b
f = float(a)/float(b)

# output
print u"%d %d %.5f" % (d, r, f)