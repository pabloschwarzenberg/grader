#Ordenar tres números
num1 = int(input("Ingrese un número"))
num2 = int(input("Ingrese otro número"))
num3 = int(input("Ingrese un último número"))

if num1 <= num2 <= num3:
    print(num1, num2, num3, sep=",")
elif num2 <= num1 <= num3:
    print(num2, num1, num3, sep=",")
elif num3 <= num1 <= num2:
    print(num3, num1, num2, sep=",")
elif num2 <= num3 <= num1:
    print(num2, num3, num1, sep=",")
elif num1 <= num3 <= num2:
    print(num1, num3, num2, sep=",")
elif num3 <= num2 <= num1:
    print(num3, num2, num1, sep=",")  