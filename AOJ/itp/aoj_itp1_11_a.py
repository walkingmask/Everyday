# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A
# 11:05 - 12:06

face = map(int, raw_input().split())
order = raw_input()

dice = [    [ 0, face[0] ],
            [ 1, face[1] ],
            [ 2, face[2] ],
            [ 3, face[3] ],
            [ 4, face[4] ],
            [ 5, face[5] ]]
temp = 0

for i in order:
    if i == 'N':
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[5][1]
        dice[5][1] = dice[4][1]
        dice[4][1] = temp
    if i == 'E':
        temp = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = dice[5][1]
        dice[5][1] = dice[2][1]
        dice[2][1] = temp
    if i == 'S':
        temp = dice[0][1]
        dice[0][1] = dice[4][1]
        dice[4][1] = dice[5][1]
        dice[5][1] = dice[1][1]
        dice[1][1] = temp
    if i == 'W':
        temp = dice[0][1]
        dice[0][1] = dice[2][1]
        dice[2][1] = dice[5][1]
        dice[5][1] = dice[3][1]
        dice[3][1] = temp

print dice[0][1]


'''
sankou ni natta kaitou
#1156867 Solution for ITP1_11_A: Dice I by cjoedwio

def rot(dice, I):
  #USEWND
  #NEWSUD
  a = dice[:]
  if I=='N': x=[0,4,5,1,0]
  elif I=='E': x=[0,2,5,3,0]
  elif I=='W': x=[0,3,5,2,0]
  elif I=='S': x=[0,1,5,4,0]
  for i in [0,1,2,3]: a[x[i+1]]=dice[x[i]]
  return a
 
dice = map(int,raw_input().split())
for c in raw_input(): dice = rot(dice,c)
print dice[0]
'''