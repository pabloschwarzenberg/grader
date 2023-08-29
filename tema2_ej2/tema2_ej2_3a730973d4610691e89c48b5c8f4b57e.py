def amigos(a,b):
    numero1=0
    for i in range(1,a):
        if a%i==0:
            numero1=numero1+i
    numero2=0
    for i in range(1,b):
        if b%i==0:
            numero2=numero2+i
    if numero1==b and numero2==a:
        return True
    return False
    
print (amigos)