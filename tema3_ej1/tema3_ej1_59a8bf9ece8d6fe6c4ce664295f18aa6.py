def suma_divisores(numero):
    div = []
    suma = 0
    for i in range(1, numero - 1):
        if (numero % i) == 0:
            div.append(i)
    for k in div:
        suma += k
    if suma == 1:
        return suma, True
    else:
        return suma, False
