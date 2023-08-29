# completa el código de la función
def suma_divisores(a):
    resultado = 0
    primo = False
    for divisores in range(1, a):
        if a%divisores == 0:
            resultado += divisores
    if resultado == 1:
        primo = True
    suma = (resultado, primo)
    return suma
           