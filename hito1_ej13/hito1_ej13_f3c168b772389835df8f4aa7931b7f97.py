#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializar el factor primo como 2
    factor_primo = 2

    while factor_primo <= numero:
        if numero % factor_primo == 0:
            # Imprimir el factor primo
            print(factor_primo)
            numero = numero // factor_primo
        else:
            factor_primo += 1

# Solicitar al usuario ingresar un número entero
numero = int(input())

# Descomponer el número en factores primos e imprimirlos
descomposicion_factores_primos(numero)
      