#Ordenar tres números
numeros = [int(input(" ingrese 1er numero : ")), int(input(" ingrese 2do numero : ")), int(input(" ingrese 3er numero: "))]
contador= 0

while (contador < len(numeros)):
  contador2 = 0
  while (contador2 < len(numeros)):
    if (numeros[contador] < numeros[contador2]):
      numeros[contador2], numeros[contador] = numeros [contador], numeros[contador2]
    contador2 += 1
  contador += 1

print(numeros)      