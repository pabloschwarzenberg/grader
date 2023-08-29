def descomposicion_factores_primos(numero):
    # Función para verificar si un número es primo
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Descomposición de factores primos
    factores_primos = []
    divisor = 2

    while numero > 1:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero //= divisor
        else:
            divisor += 1

    # Imprimir los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Solicitar al usuario un número y realizar la descomposición
numero = int(input())

descomposicion_factores_primos(numero)
