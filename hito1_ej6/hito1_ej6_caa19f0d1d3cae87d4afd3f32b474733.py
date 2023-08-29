def ordenar_numeros(num1, num2, num3):
  numeros = [num1, num2, num3]
  numeros.sort()
  return numeros
  
num1 = int(input("Ingrese el primer nuemro:"))
num2 = int(input("Ingrese el segundo numero:"))
num3 = int(input("Ingrese el tercer numero:"))

numeros_ordenados = ordenar_numeros(num1, num2, num3)
print("Loa numeros ordenados de mayor a menor:", ",".join(str(num) for num in numeros_ordenados))