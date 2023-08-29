#Ordenar tres números
 
#Entrada de datos:

num1 = int(input("Ingresa el primero numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

# Proceso y Salida de datos:

if num1 <= num2 <=num3:
    print(f"{num1} {num2} {num3}")

elif num1 <= num3 <= num2:
    print(f"{num1} {num3} {num4}")

elif num2 <= num1 <= num3:
    print(f"{num2} {num1} {num3}")

elif num2 <= num3 <= num1:
    print(f"{num2} {num3} {num1}")

elif num3 <= num1 <= num2:
    print(f"{num3} {num1} {num2}")

elif num3 <= num2 <= num1:
    print(f"{num3} {num2} {num1}")