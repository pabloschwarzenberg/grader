num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(num1, ",", num2, ",", num3)
    else:
        print(num1, ",", num3, ",", num2)
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(num2, ",", num1, ",", num3)
    else:
        print(num2, ",", num3, ",", num1)
else:
    if num1 <= num2:
        print(num3, ",", num1, ",", num2)
    else:
        print(num3, ",", num2, ",", num1)

