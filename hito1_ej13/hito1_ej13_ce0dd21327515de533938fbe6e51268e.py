#Factores Primos
def factorizar_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero /= factor
        else:
            factor += 1

# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es válido
if numero < 2:
    print("El número debe ser mayor o igual a 2.")
else:
    print("Descomposición de factores primos:")
    factorizar_primos(numero)
