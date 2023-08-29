#Ordenar tres numeros
num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))
a=min(num1,num2,num3)
b=max(num1,num2,num3)
c=(num1 + num2 + num3) - a - b
print(",",a,",",c,",",b)