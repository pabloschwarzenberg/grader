#Ordenar tres números
num1 = int(input("Ingrese El Primer Numero: "))
num2 = int(input("Ingrese El Segundo Numero: "))
num3 = int(input("Ingresa El Tercer Numero: "))

numeros = [num1, num2, num3]
numeros.sort()

print(numeros[0], ',', numeros[1], ',', numeros[2])