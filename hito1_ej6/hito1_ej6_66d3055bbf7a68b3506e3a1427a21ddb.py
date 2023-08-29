#Ordenar tres número
num1= int(input("Ingrese primer número: "))
num2= int(input("Ingrese segundo número: "))
num3= int(input("Ingrese tercer número: "))
if num1>num2 and num2>num3 or num1==num2 and num2>num3:
    print("Sus números ordenados de mayor a menor son: " + str(num3)+ "," + str(num2) + "," + str(num1))
elif num2>num1 and num1>num3 or num2==num1 and num1>num3:
     print("Sus números ordenados de mayor a menor son: " + str(num3)+ "," + str(num1) + "," + str(num2))
elif num3>num2 and num2>num1 or num3==num2 and num2>num1:
    print("Sus números ordenados de mayor a menor son: " + str(num1)+ "," + str(num2) + "," + str(num3))
elif num2>num3 and num3>num1 or num2==num3 and num3>num1:
    print("Sus números ordenados de mayor a menor son: " + str(num1)+ "," + str(num3) + "," + str(num2))
elif num3>num1 and num1>num2 or num3==num1 and num1>num2:
    print("Sus números ordenados de mayor a menor son: " + str(num2)+ "," + str(num1) + "," + str(num3))
elif num1==num2 and num3>num2 and num3>num1:
    print("Sus números ordenados de mayor a menor son: " + str(num1) + "," + str(num2) + "," + str(num3))
elif num2==num3 and num1>num2 and num1>num3:
    print("Sus números ordenados de mayor a menor son: " + str(num3) + "," + str(num2) + "," + str(num1))
elif num1==num3 and num2>num1 and num2>num3:
    print("Sus números ordenados de mayor a menor son: " + str(num1) + "," + str(num3) + "," + str(num2))
