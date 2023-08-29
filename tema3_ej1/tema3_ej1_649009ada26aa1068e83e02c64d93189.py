def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True  # Si la suma de los divisores es 1, el número es primo
    else:
        return suma, False  # Si la suma de los divisores es diferente de 1, el número no es primo
