#Ordenar tres números
num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))
num3 = int(input("Ingresa otro número entero: "))
menor = 0
medio = 0
mayor = 0
if num1 < num2 and num1 < num3:
    menor = num1
    if num3 < num2:
        medio = num3
        mayor = num2
    else:
        medio = num2
        mayor = num3
if num3 < num2 and num3 < num1:
    menor = num3
    if num1 < num2:
        medio = num1
        mayor = num2
    else:
        medio = num2
        mayor = num1
if num2 < num1 and num2 < num3:
    menor = num2
    if num3 < num1:
        medio = num3
        mayor = num1
    else:
        medio = num1
        mayor = num3
print(menor,",",medio,",",mayor)