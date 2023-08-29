#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos una lista vacía para almacenar los factores primos
    factores_primos = []

    # Iteramos desde 2 hasta la raíz cuadrada del número
    # Verificamos si es divisible por el número actual, si es así, agregamos el factor a la lista
    # y dividimos el número entre el factor hasta que ya no sea divisible
    for i in range(2, int(numero ** 0.5) + 1):
        while numero % i == 0:
            factores_primos.append(i)
            numero //= i

    # Si el número es mayor que 1, entonces es primo
    if numero > 1:
        factores_primos.append(numero)

    # Imprimimos los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Solicitamos al usuario ingresar un número entero
numero = int(input())

# Llamamos a la función de descomposición de factores primos
descomposicion_factores_primos(numero)
