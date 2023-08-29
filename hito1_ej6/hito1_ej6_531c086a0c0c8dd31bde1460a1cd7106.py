#Ordenar tres números
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    numeros_ordenados = ', '.join(map(str, numeros))
    print("Los números ordenados de menor a mayor son:", numeros_ordenados)

# Solicitar tres números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números
ordenar_numeros(numero1, numero2, numero3)
      