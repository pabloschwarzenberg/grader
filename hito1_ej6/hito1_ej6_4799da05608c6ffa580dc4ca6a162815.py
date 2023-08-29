#Ordenar tres números
num1 = eval(input('ingrese numero 1: '))
num2 = eval(input('ingrese numero 2: '))
num3 = eval(input('ingrese numero 3: '))

if num1 >= num2:
    if num1 >= num3:
        if num2 >= num3:
            print(str(num3)+','+str(num2)+','+str(num1))
        else:
            if num2 >= num1:
                print(str(num1)+','+str(num3)+','+str(num2))
if num3 >= num2:
        if num3>= num1:
            if num2>= num1:
                print(str(num1)+','+str(num2)+','+str(num3))
            else:
                if num2 >= num3:
                    print(str(num3)+','+str(num1)+','+str(num2))
if num3 >= num1:
    if num3 >= num2:
        if num1 >= num2:
            print(str(num2)+','+str(num1)+','+str(num3))
if num1 >= num2:
    if num1 >= num3:
        if num3 >= num2:
            print(str(num2)+','+str(num3)+','+str(num1))   