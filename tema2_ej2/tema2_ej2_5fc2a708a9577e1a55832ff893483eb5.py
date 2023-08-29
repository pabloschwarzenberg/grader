def amigos(n1,n2):
    a=0
    b=0
    for i in range(1,n1+1):
        if n1%i==0:
            a=a+i
    for i in range(1,n2+1):
        if n2%i==0:
            b=b+i
    if a==b and n1!=n2:
        return True
    else:
        return False