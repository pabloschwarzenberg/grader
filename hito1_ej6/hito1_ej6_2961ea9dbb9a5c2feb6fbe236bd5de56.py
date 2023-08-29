#Ordenar tres números
num1=int(input("Ingrese primer numero entero: "))
num2=int(input("Ingrese segundo numero entero: "))
num3=int(input("Ingrese tercer numero entero: " ))

a=min(num1,num2,num3)
c=max(num1,num2,num3)
b=(num1 + num2 + num3) - a - c 
