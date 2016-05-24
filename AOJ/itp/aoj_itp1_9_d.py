# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_D

in_str = raw_input()
q = input()

for i in xrange(q):
    order = raw_input().split()
    a = int(order[1])
    b = int(order[2])+1

    if order[0] == "print":
        print in_str[a:b]
    if order[0] == "reverse":
        temp_str    = in_str[a:b]
        in_str = in_str[:a] + temp_str[::-1] + in_str[b:]
    if order[0] == "replace":
        in_str = in_str[:a] + order[3] + in_str[b:]

