num1 = int(input("Escribra el primer numero: "))
num2 = int(input("Escribra el segundo numero: "))
num3 = int(input("Escribra el tercer numero: "))

a = min(num1,num2,num3)
c = max(num1,num2,num3)
b = (num1 + num2+ num3) - a - c
print(a,",",b,",",c)   