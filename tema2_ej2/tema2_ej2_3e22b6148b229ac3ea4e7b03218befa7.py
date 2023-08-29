# completa el código de la función
def amigos(a, b):
    DivA=[]
    DivB=[]
    i = 1
    k = 1
    AcumA=0
    AcumB=0
    while i<a:
        if a%i==0:
            DivA.append(i)
            AcumA = AcumA+i
        i=i+1
    while k<b:
        if b%k==0:
            DivB.append(k)
            AcumB = AcumB+k
        k=k+1
    if (AcumA==b) and (AcumB==a):
        return True
    else:
        return False