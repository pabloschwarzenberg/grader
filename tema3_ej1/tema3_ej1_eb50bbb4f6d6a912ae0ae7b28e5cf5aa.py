def suma_divisores(numero):
    suma = 0
    primo = True
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma == 1:
        primo = True
    else:
        primo = False
    return suma,primo
           