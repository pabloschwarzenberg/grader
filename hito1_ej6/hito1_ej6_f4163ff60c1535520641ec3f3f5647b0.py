#Ordenar tres números
numeros_ordenados = []
i = 0

while i < 3:
  num = int(input("Ingrese un número: "))
  numeros_ordenados.append(num)
  i += 1

numeros_ordenados.sort()
print(numeros_ordenados)