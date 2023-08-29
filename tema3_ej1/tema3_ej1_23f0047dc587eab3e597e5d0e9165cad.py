# completa el código de la función
def suma_divisores(a):
    suma=0
    for i in range (1,a):
        if a%i==0:
            suma+=i 
    if a==1:
        return suma,False
    if a<2:
        return suma,False
    elif a==2:
        return suma,True
    else:
        for i in range(2,a):
            if(a%i)==0:
                return suma,False
            elif(i==a-1):
                return suma,True
           