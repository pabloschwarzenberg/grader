def descomposicion_factores_primos(numero):
    factor_primo = 2
    while factor_primo <= numero:
        if numero % factor_primo == 0:
            print(factor_primo)
            numero = numero / factor_primo
        else:
            factor_primo += 1

# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número entero: "))

print("Descomposición en factores primos:")
descomposicion_factores_primos(numero)
