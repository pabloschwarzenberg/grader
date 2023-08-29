numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

numeros = [numero1, numero2, numero3]
numeros.sort()

numeros_ordenados = str(numeros[0])
for i in range(1, len(numeros)):
    numeros_ordenados += "," + str(numeros[i])
 
print(numeros_ordenados)