#Ordenar tres números
   # Función para ordenar los números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar los números de menor a mayor
    return numeros

# Pedir al usuario que ingrese los números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))


numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)


print("Los números ordenados de menor a mayor son:", end=" ")
for i in range(len(numeros_ordenados)):
    if i != len(numeros_ordenados) - 1:
        print(numeros_ordenados[i], end=", ")
    else:
        print(numeros_ordenados[i])   