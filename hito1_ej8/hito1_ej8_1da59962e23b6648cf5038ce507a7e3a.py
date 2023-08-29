#Descomponer un número
num=int(input("Ingrese un número: "))
num1 = num % 10
num2 = int((num % 100) /10)
num3 = int((num % 1000) /100)
num4 = int((num % 10000) /1000)
if num2==0 and num3==0 and num4==0:
    print(num1, "U")
elif num3==0 and num4==0:
    print(num2, "D +", num1, "U")
elif num4==0:
    print(num3, "C +", num2, "D +", num1, "U")
else:
    print(num4, "M +", num3, "C +", num2, "D +", num1, "U")      