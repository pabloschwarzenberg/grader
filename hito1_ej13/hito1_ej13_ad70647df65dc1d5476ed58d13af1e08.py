def descomposicion_factores_primos(numero):
    # Inicializar el divisor en 2
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            # Es un factor primo, imprimirlo
            print(divisor)
            numero = numero / divisor
        else:
            divisor += 1
numero = int(input("Ingrese un número entero: "))
descomposicion_factores_primos(numero)
      