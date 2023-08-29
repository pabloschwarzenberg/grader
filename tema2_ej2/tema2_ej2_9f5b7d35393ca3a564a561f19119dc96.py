# completa el código de la función
def amigos(a,b):
    i=1
    j=1
    sda=0
    sdb=0
    while i<=a:
        if a%i==0:
            sda=sda+i
            i=i+1
        elif a%i!=0:
            i=i+1
    while j<=b:
        if b%j==0:
            sdb=sdb+j
            j=j+1
        elif b%j!=0:
            j=j+1
    if (sda-a)==b and (sdb-b)==a:
        return True
    elif (sda-a)!=b or (sdb-b)!=a:
        return False
