# completa el código de la función
def suma_divisores(a):
    suma=0
    for i in range(1, a):
        if a%i==0:
            suma+=i
    if suma==1:
        print("La suma de los divisores de", a, "es: ", suma)
        print(a, "es un número primo.")
        return suma, True

    elif suma!=1:
        print("La suma de los divisores de", a, "es: ", suma)
        print(a, "no es un número primo.")
        return suma, False