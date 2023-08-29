# completa el código de la función
def suma_divisores(numero):
    suma = 0 
    for i in range(1, numero):
        if numero % i == 0:
            suma += i 
    primo = suma
    if primo == 1:
        return suma, True
    else:
        return suma, False