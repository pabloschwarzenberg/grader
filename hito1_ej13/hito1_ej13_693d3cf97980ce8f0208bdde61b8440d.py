def descomposicion_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor = factor + 1

numero = int(input("Ingresa un número entero: "))
print("La descomposición en factores primos de", numero, "es:")
descomposicion_factores_primos(numero)