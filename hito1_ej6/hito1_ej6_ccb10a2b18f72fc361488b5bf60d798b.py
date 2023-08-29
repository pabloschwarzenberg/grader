#Ordenar tres números
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))
num3 = int(input("ingresa un numero: "))
a = min(num1, num2, num3)
b = max(num1, num2, num3)
c = (num1 + num2 + num3) -a -b
print("",a,",",c,",",b)