#Ordenar tres números
      
num1 = int(input("ingrese un numero:"))
num2 = int(input("ingrese un numero:"))
num3 = int(input("ingrese un numero:"))

if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

print("orden",num1, ",",num2, ",",num3)