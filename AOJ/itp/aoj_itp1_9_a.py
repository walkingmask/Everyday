# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_A

w = raw_input().lower()
s = 0

while 1:

    in_str = raw_input()
    if in_str == "END_OF_TEXT":
        break

    in_str = map(str, in_str.split())

    for i in in_str:
        if i.lower() == w:
            s+=1

print s

'''
### sankou answer ###
import sys
w = raw_input()
n = 0
for t in sys.stdin.read().split():
    if t == 'END_OF_TEXT':
        break
    if t.lower() == w.lower():
        n += 1
print n
'''