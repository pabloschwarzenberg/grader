#Ordenar tres números
num1 = int(input("Deposite el primer número: "))
num2 = int(input("Deposite el segundo número: "))
num3 = int(input("Deposite el tercer número: "))
if ((num1 <= num2) and (num1 <= num3)):
    x = num1
    if (num2 <= num3):
        y = num2
        z = num2
    else:
        y = num3
        z = num2
elif ((num2 <= num1) and (num2 < num3)):
    x = num2
    if (num1 <= num3):
        y = num1
        z = num3
    else:
        y = num3
        z = num1
else:
    x = num3
    if (num1 <= num2):
        y = num1
        z = num2
    else:
        y = num2
        z = num1
print(x,",",y,",",z)