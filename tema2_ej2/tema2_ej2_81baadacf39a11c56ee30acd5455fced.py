def n1(a):
    a1=[]
    i=1
    for i in range(i,a-1):
        if a%i==0:
            a1.append(i)
            i=i+1
        else:
            i=i+1
            continue
    return sum(a1)

def n2(b):
    b1=[]
    i=1
    for i in range(i,b-1):
        if b%i==0:
            b1.append(i)
            i=i+1
        else:
            i=i+1
            continue
    return sum(b1)

def amigos(a,b):
    if a==n2(b) and b==n1(a):
        return True
    else:
        return False