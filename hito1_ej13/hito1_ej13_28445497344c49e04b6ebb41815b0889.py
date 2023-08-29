n=int(input())
a=2
primos=list()
while a<=n:
    b = 2
    c = 0
    while b < a:
        if a % b == 0:
            c = c + 1
        b = b + 1
    if c == 0:
        primos=primos+[a]
    a=a+1
e=0
while e<len(primos):
    if n%primos[e]==0:
        print (primos[e])
        n = n / primos[e]
        e=0
    else:
        e=e+1