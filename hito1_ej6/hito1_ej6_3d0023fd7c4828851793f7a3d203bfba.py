#Ordenar tres números
num1 = int(input("ingrese un numero:"))
num2 = int(input("ingrese otro numero :"))
num3 = int(input("ingrese otro numero:"))
if num1 <= num2 <= num3:
    print ("El orden de menor a mayor es:",num1,',',num2,',',num3)
elif num1 <= num3 <= num2:
    print ("El orden de menor a mayor es:",num1,',',num3,',',num2)
elif num2 <= num3 <= num1:
    print ("El orden de menor a mayor es:",num2,',',num3,',',num1)
elif num2 <= num1 <= num3:
    print ("El orden de menor a mayor es:",num2,',',num1,',',num3)
elif num3 <= num1 <= num2:
    print ("El orden de menor a mayor es:",num3,',',num1,',',num2)
elif num3 <= num2 <= num1:
    print ("El orden de menor a mayor es:",num3,',',num2,',',num1)     