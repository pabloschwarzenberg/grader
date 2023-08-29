print("Con éste programa usted podrá ordenar 3 números enteros de menor a mayor, es decir, en orden creciente, para ello favor ingresar los 3 números que desea ordenar\n")

print("Ingrese el primer número:")
num1 = int(input())

print("Ingrese el segundo número:")
num2 = int(input())

print("Ingrese el tercer número:")
num3 = int(input())

#Si 1>2 y 2>3
if num1<num2 and num2<num3:
    print("Sus números ordenados de menor a mayor son:","",num1,",","",num2,",","",num3)

#Si 2<1 y 1<3
elif(num2<num1 and num1<num3):
    print("Sus números ordenados de menor a mayor son:""",num2,",","",num1,",","",num3)

#Si 3<1 y 1<2
elif(num3<num1 and num1<num2):
    print("Sus números ordenados de menor a mayor son:""",num3,",","",num1,",","",num2)

#Si 1<3 y 3<2
elif(num1<num3 and num3<num2):
    print("Sus números ordenados de menor a mayor son:""",num1,",","",num3,",","",num2)

#Si 3<2 y 2<1
elif(num3<num2 and num2<num1):
    print("Sus números ordenados de menor a mayor son:""",num3,",","",num2,",","",num1)

#Si 2<3 y 3<1
elif(num2<num3 and num3<num1):
    print("Sus números ordenados de menor a mayor son:""",num2,",","",num3,",","",num1)

#Todos iguales
elif(num1 == num2 ==num3):
    print(num1,num2,num3)

elif(num1 ==num2 or num1>num3):
    print("Sus números ordenados de menor a mayor son:""",num3,",",num2,",",num1)

elif(num2 ==num3 or num2>num1):
    print("Sus números ordenados de menor a mayor son:""",num1,",",num2,",",num3)

elif(num1 ==num3 or num3>num2):
    print("Sus números ordenados de menor a mayor son:""",num2,",",num1,",",num3)


