#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

#Obtener los números del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

#Ordenar los números
numeros_ordenados = ordenar_numeros(num1, num2, num3)

#Imprimir los números ordenados
print("Aqui se encuentra la lista con los números ordenados de menor a mayor:", ", ".join(map(str, numeros_ordenados)))