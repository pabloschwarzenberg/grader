#ordenar tres numeros
num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))
num3 = int(input("ingrese el tercer numero:"))
a=min(num1,num2,num3)
b=max(num1,num2,num3)
c=(num1+num2+num3) - a - b
print(",",a,",",c,",",b)