# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C
# -

n = input()
lis = []
bot = 0
for i in xrange(n):
    com = raw_input()
    if   com[0] == 'i':
        lis.append(com[7:])
    elif com[6] == ' ':
        try:
            lis.pop(~lis[::-1].index(com[7:]))
        except:
            pass
    elif com[6] == 'F':
        lis.pop()
    else:
        bot += 1

print ' '.join( map(str, reversed(lis[bot:])) )

'''
jiriki deha dame datta...
sankou ni sasete moratta kaitou
#962434 Solution for ALDS1_3_C: Doubly Linked List by Sim0000

n = int(raw_input())
q = []
bottom = 0
for i in range(n):
    cmd = raw_input()
    if cmd[0] == 'i':
        q.append(cmd[7:])
    elif cmd[6] == ' ':
        try:
            q.pop(~q[::-1].index(cmd[7:]))
        except:
            pass
    elif cmd[6] == 'F':
        q.pop()
    else:
        bottom += 1
 
print(' '.join(q[bottom:][::-1]))

note
 - mojiretsu no itibu wo riyou shite hikaku suru beshi
 - lis.pop(0) dehanaku list no sentou wo sanshou shinai youni suru beshi
 - lis[::-1] = reversed(lis)
 - a=[1,2,3,4,5]
   a.index(1) -> 0
   ~a.index(1) -> -1
   a.index(5) -> 4
   ~a.index(5) -> -5
   a[::-1].index(1) -> 4
   ~a[::-1].index(1) -> -5
   a[::-1].index(5) -> 0
   ~a[::-1].index(5) -> -1
'''