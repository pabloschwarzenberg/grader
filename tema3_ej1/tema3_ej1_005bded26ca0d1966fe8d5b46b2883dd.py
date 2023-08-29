# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a - 1):
        if a % i != 0:
            continue
        suma += i
#Condiciones si es True o False
    if suma == 1:
        primo = True
    else:
        primo = False
    return suma, primo