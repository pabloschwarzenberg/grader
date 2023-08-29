# completa el código de la función
def suma_divisores(a):
    divisiones = 0
    for divisores in range(1, a):
        if a % divisores == 0:
            divisiones += divisores
    if divisiones == 1:
        primo = True
        return divisiones, primo
    else:
        primo = False
        return divisiones, primo
           