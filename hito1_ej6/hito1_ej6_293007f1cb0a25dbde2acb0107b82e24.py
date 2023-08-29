numA = int(input("Ingresa num 2: "))
numB = int(input("Ingresa num 1: "))
numC = int(input("Ingresa num 3: "))

if numA <= numB <= numC:
    print(numA,numB,numC,sep=",")   
elif numC <= numB <= numA:
    print(numC, numB, numA, sep=",")
elif numB <= numC <= numA:
    print(numB, numC, numA, sep=",")
elif numA <= numC <= numB:
    print(numA,numC,numB, sep=",")
elif numB <= numA <= numC:
    print(numB,numA,numC,sep=",")

"""
num1 = eval(input("Ingrese el 1 numero: ")) # mediano 2
num2 = eval(input("Ingrese el 2 numero: ")) # mayor 3
num3 = eval(input("Ingrese el 3 numero: ")) # menor 1

# Hoja de calculo

if num1 <= num2 and num2 <= num3:
    print(num1,",",num2,",",num3)

elif num3 <= num2 and num2 <= num1:
    print(num3,",",num2,",",num1)

elif num2 <= num1 and num1 <= num3:
    print(num2,",",num1,",",num3)

elif num2 <= num3 and num3 <= num1:
    print(num2,",",num3,",",num1)
"""

