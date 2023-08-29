def amigos(a,b):
    a1=0
    b1=0
    for i in range(1,a):
        if a%i==0:
            a1+=i
    for i in range(1,b):
        if b%i==0:
            b1+=i
    if b1==a and a1==b:
        return True
    else:
        return False

