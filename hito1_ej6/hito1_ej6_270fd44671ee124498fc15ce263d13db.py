#Ordenar tres números

num1 = int(input("ingresar el primer numero: "))
num2 = int(input("ingresar el segundo numero: "))
num3 = int(input("ingresar el tercer numero: "))

if num1 <= num2:
    if num2 <= num3:
        print(num1, ",", num2, ",", num3)
    else:
        if num1 <= num3:
            print(num1, ",", num3, ",", num2)
        else:
            print(num3, ",", num1, ",", num2)
else:
    if num1 <= num3:
        print(num2, ",", num1, ",", num3)
    else:
        if num2 <= num3:
            print(num2, ",", num3, ",", num1)
        else:
            print(num3, ",", num2, ",", num1)