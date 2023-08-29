# completa el código de la función
def suma_divisores(a):
    if a==1:
        return 0,False
    divisores=[]
    for i in range (1,a):
        if a%i==0:
            divisores.append(i)
    suma=sum(divisores)
    if suma==1:
        return suma,True 
    else:
        return suma,False
           