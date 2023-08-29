def descomposicion_factores_primos(numero):
    i = 2

    while i * i <= numero:
        if numero % i:
            i += 1
        else:
            numero //= i
            print(i)

    if numero > 1:
        print(numero)

# Ejemplo de uso
numero = int(input("Ingrese un número entero: "))
print("Descomposición de factores primos:")
descomposicion_factores_primos(numero)
