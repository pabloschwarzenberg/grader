#Ordenar tres números.

# Entradas
numero_1 = int(input("Ingrese el primero número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))

# Variables para ordenar los números
numero_menor = 0
numero_medio = 0
numero_mayor = 0

# Proceso
if (numero_1 > numero_2) and (numero_1 > numero_3):
    numero_mayor = numero_1
    if numero_2 > numero_3:
        numero_medio = numero_2
        numero_menor = numero_3
    else:
        numero_medio = numero_3
        numero_menor = numero_2
if (numero_2 > numero_1) and (numero_2 > numero_3):
    numero_mayor = numero_2
    if numero_1 > numero_3:
        numero_medio = numero_1
        numero_menor = numero_3
    else:
        numero_medio = numero_3
        numero_menor = numero_1
elif (numero_3 > numero_1) and (numero_3 > numero_2):
    numero_mayor = numero_3

    if numero_1 > numero_2:
        numero_medio = numero_1
        numero_menor = numero_2
    else:
        numero_medio = numero_2
        numero_menor = numero_1

# Salida
print(numero_menor,",",numero_medio,",",numero_mayor)