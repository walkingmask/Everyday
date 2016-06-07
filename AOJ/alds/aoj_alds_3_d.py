# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_D
# -

# input
section = raw_input()

# map the height of the section
height = 0
heights = [0]
for p in xrange( len(section) ):
    if   section[p] == '/':
        height += 1
    elif section[p] == '\\':
        height -= 1
    heights.append(height)

# search the pools
pools = []
water = []
p = 0
while p < len(section):
    if section[p] == '\\':
        try:
            pr = heights[p+1:].index( heights[p] )
            pools.append([p, p+1+pr])
            p = p+1+pr
        except:
            p+=1
    else:
        p+=1

# count
for pool in pools:
    tp = section[pool[0]:pool[1]]
    depth = 0
    s = 0
    for p in xrange( len(tp) ):
        if   tp[p] == '/':
            depth -= 1
        elif tp[p] == '\\':
            depth += 1
            s += 2*(depth-1)+1
        else:
            s += depth
    water.append(s)

# print
print sum(water)
if len(water) == 0:
    print len(water)
else:
    print len(water), " ".join(map(str, water))
