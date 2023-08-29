def amigos(a, b):
    i=1
    c=0
    d=0
    j=1
    while i<=a:
        if a%i==0:
            c=c+i
        i=i+1
    while j<=b:
        if b%j==0:
            d=d+j
        j=j+1
    if a==b:
        return False
    elif d==c:
        return True
    else:
        return False