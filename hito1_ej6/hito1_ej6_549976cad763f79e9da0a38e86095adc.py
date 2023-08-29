def ordenar_numeros(num1, num2, num3):
  numeros = [num1, num2, num3]
  numeros.sort()
  numeros_ordenados = ', '.join(map(str, numeros))
  return numeros_ordenados

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

print("Números ordenados de menor a mayor:", numeros_ordenados)
