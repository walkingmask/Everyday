# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_B

# v 2.0
while 1:
    s=raw_input()
    if s=="-": break
    for i in xrange(input()):
        h=input()
        s=s[h:]+s[:h]
    print s


'''
# v 1.0
while 1:

    string = raw_input()
    if string == "-":
        break

    l = len(string)

    for i in xrange(int(input())):

        h = int(input())

        lower  = string[0:h]
        upper  = string[h:l]

        string = upper + lower

    print string
'''

'''
# sankou
while True:
    card = raw_input().strip()
    if card =="-":
        break
    shufflenum = int(raw_input().strip())
    for x in xrange(shufflenum):
        h = int(raw_input().strip())
        card = card[h:]+card[:h]
    print card
'''