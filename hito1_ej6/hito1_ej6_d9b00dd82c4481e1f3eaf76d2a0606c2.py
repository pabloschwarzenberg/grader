print('Escriba los numeros para que sean ordenados de menor a mayor')
print('1er numero')
num1 = int(input())
print('2do numero')
num2 = int(input())
print('3er numero')
num3 = int(input())
if num1 < num2 and num1 < num3 and num2 < num3:
    print(num1,',',num2,',',num3)
elif num2 < num1 and num2 < num3 and num1 < num3:
    print(num2,',',num1,',',num3)
elif num3 < num1 and num3 < num2 and num2 < num1:
    print(num3,',',num2,',',num1)
   