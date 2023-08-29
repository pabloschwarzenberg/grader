#Ordenar tres números

num1 = eval(input("Ingrese el primer numero: "))
num2 = eval(input("Ingrese el segundo numero: "))
num3 = eval(input("Ingrese el tercer numero: "))

if(num1 <= num2 <= num3):
    print("{}, {}, {}".format(num1, num2, num3))

elif(num1 <= num3 <= num2):
    print("{}, {}, {}".format(num1, num3, num2))

elif(num2 <= num1 <= num3):
    print("{}, {}, {}".format(num2, num1, num3))

elif(num2 <= num3 <= num1):
    print("{}, {}, {}".format(num2, num3, num1))

elif(num3 <= num1 <= num2):
    print("{}, {}, {}".format(num3, num1, num2))

elif(num3 <= num2 <= num1):
    print("{}, {}, {}".format(num3, num2, num1))
