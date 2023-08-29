# Solicitar los números al usuario
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

# Ordenar los números de menor a mayor
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

# Imprimir los números ordenados
numeros_ordenados = str(numero1) + ', ' + str(numero2) + ', ' + str(numero3)
print('Números ordenados de menor a mayor:', numeros_ordenados)
