print("Ingrese el primer número: ")
numero1 = int(input())
print("Ingrese el segundo número: ")
numero2 = int(input())
print("Ingrese el tercer número: ")
numero3 = int(input())

numeros = [numero1, numero2, numero3]
numeros.sort()

print("Números ordenados:", end=" ")
for i in range(len(numeros)):
    if i != len(numeros) - 1:
        print(numeros[i], end=", ")
    else:
        print(numeros[i])
