# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A
# 10:40 - 10:53
# Reverse Polish Notation with stack

rpn = map(str, raw_input().split())
stack = []

for i in rpn:
    if i.isdigit():
        stack.append(i)
    else:
        n1 = int( stack.pop() )
        n2 = int( stack.pop() )

    if   i == '+':
        stack.append( str(n2+n1) )
    elif i == '-':
        stack.append( str(n2-n1) )
    elif i == '*':
        stack.append( str(n2*n1) )

print stack[0]

'''
nice code using try and except
#688192 Solution for ALDS1_3_A: Stack by cjoedwio

x = raw_input().split()
s = []
for e in x:
    try:
        s.append(int(e))
    except:
        b = s.pop()
        a = s.pop()
        if e == '+':
            s.append(a+b)
        if e == '-':
            s.append(a-b)
        if e == '*':
            s.append(a*b)
print s.pop()
'''