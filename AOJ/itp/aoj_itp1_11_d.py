# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_D
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
    flag = 0
    for i in xrange(4):
        for j in xrange(4):
            flag += 1 if dice1 == dice2 else 0
            dice2 = rspin(dice2)
        dice2 = s2n(dice2)

    dice2 = w2e(dice2)
    for i in xrange(4):
        flag += 1 if dice1 == dice2 else 0
        dice2 = rspin(dice2)

    dice2 = w2e(dice2)
    dice2 = w2e(dice2)
    for i in xrange(4):
        flag += 1 if dice1 == dice2 else 0
        dice2 = rspin(dice2)
    return flag

# MAIN
dices = []
# input the dices
n = input()
for i in xrange(n):
    dices.append( map(int, raw_input().split()) )

# processing
for i in xrange(n-1):
    for j in xrange(i+1,n):
        if isd(dices[i], dices[j]) > 0:
            print "No"
            exit()
print "Yes" 

