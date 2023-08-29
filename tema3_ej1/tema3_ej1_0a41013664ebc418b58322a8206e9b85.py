def suma_divisores(a):
    suma = 0
    valor2 = True
    for div in range(1,a):
        if a%div == 0:
            suma = suma + div
    if suma < 2:
        valor2 = False
    elif suma == 2:
        valor2 = True
    else:
        for i in range(2, suma):
            if suma % i == 0:
                valor2 = False
        valor2 = True
    return (suma,valor2)