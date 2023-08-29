__author__ = 'Damian'
def suma_divisores(b):
    suma=0
    for i in range(1 ,b):
        if b%i==0:
            suma+=i
    if suma==1:
        print("La suma de los divisores de", b, "es: ", suma)
        print(b, "es un número primo.")
        return suma, True

    elif suma!=1:
        print("La suma de los divisores de", b, "es: ", suma)
        print(b, "no es un numero primo.")
        return suma, False