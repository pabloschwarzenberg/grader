# completa el código de la función
def suma_divisores(a):
    b= a-1
    suma=0
    for i in range(1,b):
        if (a % i) == 0:
            suma = suma + i
        else:
            continue
          
    if suma == 1:
        primo = True
    else:
        primo = False
                   
    return suma,primo

           