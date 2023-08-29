#Ordenar tres números
numeros = []

for i in range(3):
  numeros.append(int(input()))
  
numeros.sort()
salida = str(numeros[0])

for i in numeros[1:]:
  salida = salida + ',' + str(i)
  
print(salida)