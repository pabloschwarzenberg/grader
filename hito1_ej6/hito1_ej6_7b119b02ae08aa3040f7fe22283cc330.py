#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num1, num2, num3, sep=", ")
    else:
        print(num1, num3, num2, sep=", ")
elif num2 < num1 and num2 < num3:
    if num1 < num3:
        print(num2, num1, num3, sep=", ")
    else:
        print(num2, num3, num1, sep=", ")
else:
    if num1 < num2:
        print(num3, num1, num2, sep=", ")
    else:
        print(num3, num2, num1, sep=", ")