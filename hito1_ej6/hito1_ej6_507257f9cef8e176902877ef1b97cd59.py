#Ordenar tres números
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
num3 = int(input("Ingresa otro numero: "))

if num1>num2 and num2>num3:
    print("El orden de los numeros es: ",num3,",", num2,",", num1)
elif num1>num3 and num3>num2:
    print("El orden de los numeros es: ",num2,",", num3,",", num1)
elif num2>num1 and num1>num3:
    print("El orden de los numeros es: ",num3,",", num1,",", num2)
elif num2>num3 and num3>num1:
    print("El orden de los numeros es: ",num1,",", num3,",", num2)
elif num3>num1 and num1>num2:
    print("El orden de los numeros es: ",num2,",", num1,",", num3)
elif num3==num1 and num3>num2:
    print("El orden de los numeros es: ",num2,",", num1,",", num3)
elif num3==num1 and num3<num2:
    print("El orden de los numeros es: ",num3,",", num1,",", num2)
elif num3==num2 and num3>num1:
    print("El orden de los numeros es: ",num1,",", num2,",", num3)
elif num3==num2 and num3<num1:
    print("El orden de los numeros es: ",num3,",", num2,",", num1)
elif num1==num2 and num1>num3:
    print("El orden de los numeros es: ",num3,",", num2,",", num1)
elif num1==num2 and num1<num3:
    print("El orden de los numeros es: ",num1,",", num2,",", num3)
elif num1==num2==num3:
    print("El orden de los numeros es: ",num3,",", num2,",", num1)
else:
    print("El orden de los numeros es: ",num1,",", num2,",", num3)
