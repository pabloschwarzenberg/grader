# Pedir 3 numeros al programa
num1 = int(input("Ingresar primer número:"))
num2 = int(input("Ingresar segundo número:"))
num3 = int(input("Ingresar tercer número:"))

# Ordenar los números de menos a mas, usando if, else
if num1 <= num2:
    if num2 <= num3:
        print(num1, ",", num2, ",", num3)
    else:
        if num1 <= num3:
            print(num1, ",", num3, ",", num2)
        else:
            print(num3, ",", num1, ",", num2)
else:
    if num1 <= num3:
        print(num2, ",", num1, ",", num3)
    else:
        if num2 <= num3:
            print(num2, ",", num3, ",", num1)
        else:
            print(num3, ",", num2, ",", num1)