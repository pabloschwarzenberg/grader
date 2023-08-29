#Ordenar tres números
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

if num1>=num2>=num3:
    print(num3,",",num2,",",num1)
if num1>=num3>=num2:
    print(num2, ",", num3, ",", num1)
if num2>=num1>=num3:
    print(num3, ",", num1, ",", num2)
if num2>=num3>=num1:
    print(num1, ",", num3, ",", num2)
if num3>=num2>=num1:
    print(num1, ",", num2, ",", num3)
if num3>=num1>=num2:
    print(num2, ",", num1, ",", num3)