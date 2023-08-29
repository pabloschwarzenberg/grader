#Ordenar tres números
num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))
num3=int(input("Ingresa el tercer número: "))

numeros=[num1, num2, num3]
numeros.sort()

print("{}, {}, {}".format(numeros[0], numeros[1], numeros[2]))
  