def amigos(a,b):
    sumaa=0
    sumab=0
    for i in range(1,a):
        if a%i==0:
            sumaa=sumaa+i
    for n in range(1,b):
        if b%n==0:
            sumab=sumab+n
    return sumaa==b and sumab==a    