# completa el código de la función
def suma_divisores(numero): #numero=6   => divisores= 1,2,3
    suma = 0 #acumula divisores
    x=1
    while (x<numero): #x=0,1,2,3,4,5
        if numero%x==0:
            suma = suma + x #acumula el vivisor que encuentra
        x= x+1
    if suma == 1:
        esPrimo =  1  #es primo
    else:
        esPrimo =  0  #no es primo
    return suma, esPrimo    #retorna el resultado de la funcion
           