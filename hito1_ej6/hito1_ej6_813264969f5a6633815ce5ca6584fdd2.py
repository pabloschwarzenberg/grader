#Solicitar los numeros al usuario
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
#Ordenar los numeros de menor a mayor
numeros = [numero1, numero2, numero3]
numeros.sort()
#Imprimir los números ordenados separados por comas
print("Números ordenados:", end=" ")
for i in range(len(numeros)):
    if i != len(numeros) - 1:
        print(numeros[i], end=", ")
    else:
        print(numeros[i])
