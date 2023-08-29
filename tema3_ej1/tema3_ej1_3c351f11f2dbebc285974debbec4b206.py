# completa el código de la función
def suma_divisores(a):
    aux= a-1
    suma=0

    while aux!=0:
        if a % aux == 0:
            suma=suma+aux

        aux = aux - 1
    return suma,suma==1
           