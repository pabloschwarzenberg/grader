def descomposicion_factores_primos(numero):
    # Inicializar la lista de factores primos
    factores_primos = []

    # Dividir el número entre 2 hasta que ya no sea divisible
    while numero % 2 == 0:
        factores_primos.append(2)
        numero //= 2

    # Dividir el número entre los números impares comenzando desde 3
    # hasta la raíz cuadrada del número, de 2 en 2
    for i in range(3, int(numero**0.5) + 1, 2):
        while numero % i == 0:
            factores_primos.append(i)
            numero //= i

    # Si el número que queda es mayor que 2, es un factor primo
    if numero > 2:
        factores_primos.append(numero)

    # Imprimir los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Pedir al usuario un número
numero = int(input("Ingrese un número: "))

# Obtener la descomposición de factores primos e imprimirlos
descomposicion_factores_primos(numero)
