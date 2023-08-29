# completa el código de la función
def amigos(a,b):
    suma=0
    for i in range(1,a):
        if a%i==0:
            div=i
            suma+=div
    if suma==b:
        return True
    else:
        return False
    
    print(suma)


           