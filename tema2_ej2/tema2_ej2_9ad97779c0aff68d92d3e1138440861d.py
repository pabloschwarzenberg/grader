def amigos(a,b):
    i=1
    h=0
    while i<=a:
        if a%i==0:
            h=h+i
        i=i+1

    m=1
    n=0

    while m<=b:
        if b%m==0:
            n=n+m
        m=m+1
   
    if n==h and a!=b:
        return True
    else:
        return False
