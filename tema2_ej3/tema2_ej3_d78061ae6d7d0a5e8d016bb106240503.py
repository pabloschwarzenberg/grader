def numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == numero:
        return True  # El número es perfecto
    else:
        return False  # El número no es perfecto
