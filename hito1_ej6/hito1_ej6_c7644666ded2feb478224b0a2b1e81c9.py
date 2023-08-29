#Ordenar tres números
aux = 0

num1 = int(input("Ingresa el primer número: "))
while(num1 <= 0):
    num1 = int(input("El valor debe ser mayor a 0. Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
while(num2 <= 0):
    num2 = int(input("El valor debe ser mayor a 0. Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
while(num3 <= 0):
    num3 = int(input("El valor debe ser mayor a 0. Ingresa el tercer número:"))

while(num1 > num2 or num2 > num3):
    if (num2 > num3):
        aux = num3
        num3 = num2
        num2 = aux
    aux = num2
    num2 = num1
    num1 = aux
    while(num2 > num3):
        aux = num3
        num3 = num2
        num2 = aux
print(str(num1)+","+str(num2)+","+str(num3))