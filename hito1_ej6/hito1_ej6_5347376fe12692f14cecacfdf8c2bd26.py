#Ordenar tres números

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))


if num1 <= num2 and num2 <= num3:
     resultado = num1, num2, num3
elif num2 <= num1 and num1 <= num3:
    resultado = num2, num1, num3
elif num3 <= num1 and num1 <= num2:
    resultado = num3, num1, num2
elif num1 <= num3 and num3 <= num2:
    resultado = num1, num3, num2
elif num2 <= num3 and num3 <= num1:
    resultado = num2, num3, num1
elif num3 <= num2 and num2 <= num1:
    resultado = num3, num2, num1

print(resultado)