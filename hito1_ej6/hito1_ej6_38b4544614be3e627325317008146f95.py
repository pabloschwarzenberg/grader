#Ordenar tres números
num1 = int(input("ingresa un número: "))

num2 = int(input("Ingrese un segundo número: "))

num3 = int(input("Ingrese un último número: "))

if num1 <= num2 and num2 <= num3:
    print(num1, ",", num2, ",", num3)
elif num2 <= num1 and num1 <= num3:
    print(num2, ",", num1, ",", num3)
elif num3 <= num1 and num1 <= num2:
    print(num3, ",", num1, ",", num2)
elif num3 <= num2 and num2 <= num1:
    print(num3, ",", num2, ",", num1)
elif num1 <= num3 and num3 <= num2:
    print(num1, ",", num3, ",", num2)
elif num2 <= num3 and num3 <= num1:
    print(num2, ",", num3, ",", num1)
else:
    print("Los números ingresados no son compatibles.")