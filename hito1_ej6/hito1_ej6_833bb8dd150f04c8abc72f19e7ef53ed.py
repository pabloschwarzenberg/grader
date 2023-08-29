#Ordenar tres números
num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))

a = min(num1,num2,num3)
c = max(num1,num2,num3)
b = (num1 + num2 + num3) - a - c

print("Los numeros ordenados son: ",a,",",b,",",c)