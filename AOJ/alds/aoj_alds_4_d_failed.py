# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_D
# -
# Allocation
# failed

# functions
# moving the item from start trug from stop trug
def moveRight(trug, start, stop):
    # when the start has 2 or more items
    if trug[start][1]-trug[start][0] > 1:
        for i in xrange(stop-start):
            trug[start+i][1] -= 1
            trug[start+i+1][0] -= 1

def moveLeft(trug, start, stop):
    # when the start has 2 or more items
    if trug[start][1]-trug[start][0] > 1:
        for i in xrange(start-stop):
            trug[start-i][0] += 1
            trug[start-i-1][1] += 1

# calculating the total weight of the items for each trugs
def calcWeight(trug, w):
    temp = [ sum(w[trug[i][0]:trug[i][1]]) for i in xrange(len(trug)) ]
    return temp

# test function
def printTrug(trug, w):
    print calcWeight(trug, w)

def printTrug2(trug, w):
    print [ w[trug[i][0]:trug[i][1]] for i in xrange(len(trug)) ]

# input
n, k = map(int, raw_input().split())
w = []
for i in xrange(n):
    w.append(input())

# temp allocated
if k == 1:
    trug = [[0, n]]
else:
    ta = n/k
    trug = [[i*ta, ta+i*ta] for i in xrange(k-1)]
    trug.append([(i+1)*ta, n])

# processing
trugw = calcWeight(trug, w) # the total weights of the trugs
maxt  = max(trugw)          # the max weight of the trugs
imaxt = trugw.index(maxt)   # the index of the max
mint  = min(trugw)          # the min weight of the trugs
imint = trugw.index(mint)   # the index of the min

printTrug2(trug, w)
printTrug(trug, w)

while True:
    if   imaxt == imint:
        break
    # when the max is to the left of the min
    elif imaxt < imint:
        # when the min added the item is less then the max 
        if mint+w[trug[imint-1][1]-1] < maxt:
            moveRight(trug, imaxt, imint)
    # when the max is to the right of the min
    else:
        # when the min added the item is less then the max 
        if mint+w[trug[imint+1][0]] < maxt:
            moveLeft(trug, imaxt, imint)
    
    # recalculation
    trugw = calcWeight(trug, w)
    n = max(trugw) # the new max weight
    # the exit conditions
    if n >= maxt:
        break
    else:
        maxt  = n
        imaxt = trugw.index(maxt)
        mint = min(trugw)
        imint = trugw.index(mint)

    printTrug2(trug, w)
    printTrug(trug, w)

print maxt
