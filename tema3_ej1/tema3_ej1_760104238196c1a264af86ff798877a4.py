# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a // 2 + 1):
        if a // i == a / i:
            suma += i
    if suma == 1:
        primo = True
    else:
        primo = False
    return suma, primo
