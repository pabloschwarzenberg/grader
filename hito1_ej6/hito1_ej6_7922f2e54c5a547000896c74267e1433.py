#Ordenar tres números
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))
num3 = int(input("Ingrese un ultimo numero entero: "))

if num1>=num2 and num2>=num3:
    print(num3 ,",", num2 ,",", num1)
elif num2>=num1 and num1>=num3:
    print(num3 ,",", num1 ,",", num2)
elif num3>=num1 and num1>=num2:
    print(num2 ,",", num1 ,",", num3)
elif num3>=num2 and num2>=num1:
    print(num1 ,",", num2 ,",", num3)
elif num1>=num3 and num3>=num2:
    print(num2 ,",", num3 ,",", num1)
elif num2>=num3 and num3>=num1:
    print(num1 ,",", num3 ,",", num2)
else:
    print("hay numeros iguales")