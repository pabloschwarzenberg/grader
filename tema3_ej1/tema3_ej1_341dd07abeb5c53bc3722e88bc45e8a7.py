# completa el código de la función
def suma_divisores(a):
    i = 1
    div = []
    while i < a:
        if a % i == 0:
            div.append(i)
        i += 1
    i = 0
    suma = 0
    while i < len(div):
        suma += div[i]
        i += 1
    if suma == 1:
        primo = True
    if suma !=1:
        primo = False
    return suma, primo