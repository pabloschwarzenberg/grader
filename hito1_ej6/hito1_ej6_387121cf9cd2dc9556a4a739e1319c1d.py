#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
  numeros = [num1, num2, num3]
  numeros.sort()
  return numeros

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

numeros_ordenados = ordenar_numeros(num1, num2, num3)
print("Números ordenados de menor a mayor:", numeros_ordenados)