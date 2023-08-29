# completa el código de la función
def suma_divisores(a):
    suma=0
    for numeros in range(1, a):
        if a % numeros == 0:
            suma += numeros
    primo = suma
    if primo == 1:
        return suma, True
    else:
        return suma, False
           