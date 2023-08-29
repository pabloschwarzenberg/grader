def numero_perfecto(numero):
    suma_divisores = 0

    # Iterar desde 1 hasta número-1
    for i in range(1, numero):
        # Verificar si i es divisor de numero
        if numero % i == 0:
            suma_divisores += i

    # Determinar si el número es perfecto
    if suma_divisores == numero:
        return True
    else:
        return False

           