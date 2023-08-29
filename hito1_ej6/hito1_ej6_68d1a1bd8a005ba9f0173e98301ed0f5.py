#Ordenar tres números
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese un número: '))
num3 = int(input('Ingrese un número: '))

if num1 >= num2 >= num3 :
    print('{},{},{}'.format(num3, num2, num1))

if num3 >= num2 >= num1 :
    print('{},{},{}'.format(num1, num2, num3))

if num2 >= num1 >= num3 :
    print('{},{},{}'.format(num3, num1, num2))

if num2 >= num3 >= num1 :
    print('{},{},{}'.format(num1, num3, num2))

if num1 >= num3 >= num2 :
    print('{},{},{}'.format(num2, num3, num1))

if num3 >= num1 >= num2 :
    print('{},{},{}'.format(num2, num1, num3))     