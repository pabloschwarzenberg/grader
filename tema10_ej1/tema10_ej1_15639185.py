def mcd (a,b,aux=0):
    if (a>b) and (a%b == 0) and aux == 0:
        return b
    if (a>b)and (a%b != 0):
        return mcd (b,a%b,aux+1)
    else:
        return b
    
    if (b>a) and (b%a == 0) and aux == 0:
        return a
    if (b>a) and (b%a != 0):
        return mcd (a,b%a,aux+1)
    else:
        return a
    
a=int(input("Inserte el primer numero: "))
b=int(input("Inserte el segundo numero: "))
mcd(a,b)
print ("El MCM es", a*b/mcd(a,b)) 