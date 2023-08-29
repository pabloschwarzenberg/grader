num1 = eval(input('Ingrese el primer número: '))
num2 = eval(input('Ingrese el segundo número: '))
num3 = eval(input('Ingrese el tercer número: '))
 
if num1 < num2 < num3:
    print(str(num1) + ',' + str(num2) + ',' + str(num3))
elif num1 < num3 < num2:
    print(str(num1) + ',' + str(num3) + ',' + str(num2))
elif num2 < num1 < num3:
    print(str(num2) + ',' + str(num1) + ',' + str(num3))
elif num2 < num3 < num1:
    print(str(num2) + ',' + str(num3) + ',' + str(num1))
elif num3 < num2 < num1:
    print(str(num3) + ',' + str(num2) + ',' + str(num1))
elif num3 < num1 < num2:
    print(str(num3) + ',' + str(num1) + ',' + str(num2))
elif num1 == num2 < num3:
    print(str(num1) + ',' + str(num2) + ',' + str(num3))
elif num3 == num2 < num1:
    print(str(num2) + ',' + str(num3) + ',' + str(num1))
elif num1 == num3 < num2:
    print(str(num1) + ',' + str(num3) + ',' + str(num2))
elif num1 == num3 > num2:
    print(str(num2) + ',' + str(num1) + ',' + str(num3))