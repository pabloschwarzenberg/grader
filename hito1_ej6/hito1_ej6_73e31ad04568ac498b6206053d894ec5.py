#Ordenar tres números
print("ORDENAR NUMEROS DE MENOR A MAYOR")
print("ingresar el primer numero: ")
num1 = int(input())
print("ingresar el segundo numero: ")
num2 = int(input())
print("ingresar el tercer numero: ")
num3 = int(input())

numeros = [num1, num2, num3]

numeros.sort()
print("Numeros ordenados de menor a mayor", numeros)      