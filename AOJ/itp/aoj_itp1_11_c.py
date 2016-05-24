# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_C
# -

# move the dice from south to north
def s2n(dice):
    aft_dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    return aft_dice

# move the dice from west to east
def w2e(dice):
    aft_dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    return aft_dice

# spin the dice to right
def rspin(dice):
    aft_dice = [dice[0],dice[2],dice[4],dice[1],dice[3],dice[5]]
    return aft_dice

# is same dice ?
def isd(dice1, dice2):
    if dice1 == dice2:
        return 1
    return 0

# input
dice1 = map(int, raw_input().split())
dice2 = map(int, raw_input().split())

# same or not flag
flag = 0

# processing
for i in xrange(4):
    for j in xrange(4):
        flag += isd(dice1, dice2);
        dice2 = rspin(dice2)
    dice2 = s2n(dice2)

dice2 = w2e(dice2)
for i in xrange(4):
    flag += isd(dice1, dice2)
    dice2 = rspin(dice2)

dice2 = w2e(dice2)
dice2 = w2e(dice2)
for i in xrange(4):
    flag += isd(dice1, dice2)
    dice2 = rspin(dice2)

# output
if flag == 0:
    print "No"
else:
    print "Yes"
