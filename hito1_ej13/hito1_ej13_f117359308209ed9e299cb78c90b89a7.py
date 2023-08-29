def descomposicion_factores_primos(numero):
    factor = 2
    while factor * factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        else:
            factor += 1
    if numero > 1:
        print(numero)

numero = int(input("Ingresa un número entero: "))
print("La descomposición de factores primos de", numero, "es:")
descomposicion_factores_primos(numero)
