num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

numeros = [num1, num2, num3]
numeros.sort()

print(str(numeros[0]) + ", " + str(numeros[1]) + ", " + str(numeros[2]))
