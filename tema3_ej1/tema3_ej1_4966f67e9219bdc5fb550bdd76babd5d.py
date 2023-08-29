def suma_divisores(numero):
    suma_div = 0
    primo = False
    for i in range(1, numero):
        if numero % i == 0:
            suma_div = suma_div + i 
    if suma_div == 1:
        primo = True
    return(suma_div, primo)
