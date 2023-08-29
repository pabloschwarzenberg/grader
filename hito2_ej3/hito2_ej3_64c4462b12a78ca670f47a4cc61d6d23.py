def ss(s,n):
    a = []
    for i in range(len(s)):
        if s[i:n+i] not in a and len(s[i:n+i]) == n:
            c = s.count(s[i:n+i])
            if c <= 1:
                a.append(s[i:n+i])
    if a.count('AAA') == 1:
        a = []
    if len(a) > 0:
        for i in a:
            print(i)
    else:
        print('ninguna')

s = input()
n = int(input())
ss(s,n)
