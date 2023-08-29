#Factores Primos
def descomposicion_factores_primos(numero):
    # Variable para almacenar los factores primos
    factores_primos = []

    # Dividir el número por 2 hasta que ya no sea divisible
    while numero % 2 == 0:
        factores_primos.append(2)
        numero = numero // 2

    # Dividir el número por los siguientes números impares
    # desde 3 hasta la raíz cuadrada del número, incrementando de 2 en 2
    i = 3
    while i * i <= numero:
        while numero % i == 0:
            factores_primos.append(i)
            numero = numero // i
        i += 2

    # Si queda un número mayor a 2, es un factor primo
    if numero > 2:
        factores_primos.append(numero)

    # Imprimir los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Solicitar al usuario ingresar un número entero
numero = int(input())

# Llamar a la función para imprimir la descomposición en factores primos
descomposicion_factores_primos(numero)
