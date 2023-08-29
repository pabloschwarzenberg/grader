#Descomponer un número
num = int(input('\nIngrese un número: '))

u = int(num%10)

num1 = (num/10)-(u/10)

d = int(num1%10)

num2 = (num1/10)-(d/10)

c = int(num2%10)

num3 = (num2/10)-(c/10)

m = int(num3)

print('\n', m,'M+', c,'C+', d,'D+', u,'U') 