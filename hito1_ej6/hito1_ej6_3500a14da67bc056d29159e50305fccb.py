#Ordenar tres números
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))

if num1>num2:
  num1, num2 = num2, num1
if num2 > num3:
  num2, num3 = num3, num2
if num1 > num2:
  num1, num2 = num2, num1
  
print("Los números ordenados de menor a mayor son:", num1, ",", num2, ",", num3)