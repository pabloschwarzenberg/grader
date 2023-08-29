# completa el código de la función
def amigos(a,b):
    suma=0
    divisores=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
            print(i)
       


    for i in range(1,b):
        if b%i==0:
            divisores=divisores+i
            print(i)
           

    if suma==b and divisores==a:
        return True
    
    else:
        return False

            