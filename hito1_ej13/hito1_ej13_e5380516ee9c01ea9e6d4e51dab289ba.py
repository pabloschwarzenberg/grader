def descomposicion_factores_primos(numero):
    # Verificar si el número es divisible por 2
    while numero % 2 == 0:
        print(2)
        numero = numero // 2

    # Verificar para los factores primos impares
    for i in range(3, int(numero**0.5) + 1, 2):
        while numero % i == 0:
            print(i)
            numero = numero // i

    # Si el número es primo y es mayor a 2
    if numero > 2:
        print(numero)


# Solicitar al usuario que ingrese un número entero
numero = int(input())

# Realizar la descomposición de factores primos
descomposicion_factores_primos(numero)

      