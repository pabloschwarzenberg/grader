def amigos(a,b):
    s=0
    for n in range(1,a):
        if a%n==0:
            s=s+n
    t=0
    for n in range(1,b):
        if b%n==0:
            t=t+n
    if s==b and t==a and a!=b:

        return True
    else:
        return False