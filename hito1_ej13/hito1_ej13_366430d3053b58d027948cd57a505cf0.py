# Factores primos 
# Entrada
numero = int(input("Ingrese numero: "))

# Proceso
if numero > 1:
    factor = 2
    while numero > 1:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        elif numero % factor != 0:
            factor += 1
# Salida 
else:
    if numero == 1: 
        print("Numero invalido")