def numero_perfecto(numero):
    suma_divisores = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor

    if suma_divisores == numero:
        return True
    else:
        return False
