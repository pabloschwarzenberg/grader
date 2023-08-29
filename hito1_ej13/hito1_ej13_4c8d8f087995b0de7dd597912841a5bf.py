def factores_primos(numero):
    i = 2
    while i <= numero:
        if numero % i == 0:
            print(i)
            numero = numero // i
        else:
            i += 1

# Solicitar al usuario ingresar un número
numero = int(input())

# Realizar la descomposición de factores primos
factores_primos(numero)
