#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializamos el divisor en 2
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            # Si el número es divisible por el divisor, es un factor primo
            print(divisor)
            numero = numero / divisor
        else:
            # Si no es divisible, incrementamos el divisor
            divisor += 1

# Pedimos al usuario que ingrese un número
numero = int(input("Ingresa un número entero: "))

print("La descomposición de factores primos de", numero, "es:")
descomposicion_factores_primos(numero)
