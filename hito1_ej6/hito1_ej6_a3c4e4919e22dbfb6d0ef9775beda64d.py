#Ordena de menor a mayor, separados por una coma.

num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))
num3 = int(input("Ingrese el número 3: "))

if num1 <= num2 and num2 <= num3:
    print(num1,",",num2,",", num3)

elif num1 <= num3 and num3 <= num2:
    print(num1,",",num3,",", num2)

elif num2 <= num1 and num1 <= num3:
    print(num2,",",num1,",", num3)

elif num2 <= num3 and num3 <= num1:
    print(num2,",",num3,",", num1)

elif num3 <= num1 and num1 <= num2:
    print(num3,",",num1,",", num2)

elif num3 <= num2 and num2 <= num1:
    
    print(num3,",",num2,",", num1)