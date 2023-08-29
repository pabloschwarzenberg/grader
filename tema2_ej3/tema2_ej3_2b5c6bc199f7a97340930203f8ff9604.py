def numero_perfecto(numero):
    suma = 0
    divisor = numero
    if numero == 1:
        return False
    while divisor > 1:
        divisor += -1
        if numero % divisor == 0:
            suma += divisor
    if suma==numero:
        return True
    else:
        return False

           