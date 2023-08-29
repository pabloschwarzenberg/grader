def amigos(numero,numero2):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma ==1:
        suma
    suma2 = 0
    for i in range(1, numero2):
        if numero2 % i == 0:
            suma2 += i
    if suma2 ==1:
        suma2
    elif suma !=suma2:
        return False
    else:
        return True