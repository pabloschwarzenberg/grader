def descomposicion_factores_primos(numero):
    factor = 2

    while numero > 1:
        if numero % factor == 0:
            print(factor)
            numero /= factor
        else:
            factor += 1

numero = int(input("Ingresa un número entero: "))

print("La descomposición de factores primos de", numero, "es:")
descomposicion_factores_primos(numero)
