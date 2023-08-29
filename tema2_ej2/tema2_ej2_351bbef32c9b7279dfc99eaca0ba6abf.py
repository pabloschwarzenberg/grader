def amigos(a, b):
    DiA=[]
    DiB=[]
    i = 1
    k = 1
    AcuA=0
    AcuB=0
    while i<a:
        if a%i==0:
            DiA.append(i)
            AcuA = AcuA+i
        i=i+1
    while k<b:
        if b%k==0:
            DiB.append(k)
            AcuB = AcuB+k
        k=k+1
    if (AcuA==b) and (AcuB==a):
        return True
    else:
        return False