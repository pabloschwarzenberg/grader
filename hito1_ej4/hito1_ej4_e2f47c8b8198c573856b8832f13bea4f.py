def decimal_a_binario(decimal):
    binario = 0
    multiplicador = 1

    while decimal != 0:
        binario = binario + decimal % 2 * multiplicador
        decimal //= 2
        multiplicador *= 10

    return binario
decimal=int(input("Ingresa un numero entero: "))
print("resultado=",decimal_a_binario(decimal))


