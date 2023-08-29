numeros = []
contador = 1
while len(numeros) < 3:
    numero_como_cadena = input("Ingrese el número " + str(contador) + ": ")
    numero = int(numero_como_cadena)
    numeros.append(numero)
    contador = contador + 1
   

for i in numeros:
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
            
print(numeros[0],",",numeros[1],",",numeros[2])