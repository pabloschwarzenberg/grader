# completa el código de la función
def suma_divisores(a):
    divisores=[1]
    for i in range (2,a+1):
        if a%i ==0:
            divisores.append(i)
    suma=sum(divisores)- a
    if suma==1:
        p= True
    else:
        p= False
    return suma,p
           