#Ordenar tres números
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un numero entero: "))
num3 = int(input("Ingrese un numero entero: "))
if (num1 <= num2) and (num1<num3):
    
    if num2 <= num3:
        print("El orden de los números de menor a mayor es: "+str(num1)+","+str(num2)+","+str(num3))
    else:
        print("El orden de los números de menor a mayor es: "+str(num1)+","+str(num3)+","+str(num2))
if (num2 <= num1) and (num2 <= num3):
    
    if num1 <= num3:
        print("El orden de los números de menor a mayor es: "+str(num2)+","+str(num1)+","+str(num3))
    else:
        print("El orden de los números de menor a mayor es: "+str(num2)+","+str(num3)+","+str(num1))
if (num3 <= num1) and (num3 <= num2):
    if num1 < num2:
        print("El orden de los números de menor a mayor es: "+str(num3)+","+str(num1)+","+str(num2))
    else:
        print("El orden de los números de menor a mayor es: "+str(num3)+","+str(num2)+","+str(num1))