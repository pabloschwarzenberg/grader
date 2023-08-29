#DEFINICION
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

#PROCESO
if num1 <= num2 <= num3:
    num_menor, num_medio, num_mayor = num1, num2, num3
elif num1 <= num3 <= num2:
    num_menor, num_medio, num_mayor = num1, num3, num2
elif num2 <= num1 <= num3:
    num_menor, num_medio, num_mayor = num2, num1, num3
elif num2 <= num3 <= num1:
    num_menor, num_medio, num_mayor = num2, num3, num1
elif num3 <= num1 <= num2:
    num_menor, num_medio, num_mayor = num3, num1, num2
else:
    num_menor, num_medio, num_mayor = num3, num2, num1

#SALIDA
resultado = (num_menor, num_medio, num_mayor)
print("Ordenados:", resultado[0], ",", resultado[1], ",", resultado[2])
