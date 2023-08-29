#Ordenar tres números
num1=int(input("Ingrese un número entero: "))
num2=int(input("Ingrese un número entero: "))
num3=int(input("Ingrese un número entero: "))

min=min(num1, num2, num3)
max=max(num1, num2, num3)
med=(num1+num2+num3)-max-min

print("La secuencia de números de menor a mayor es: " + str(min) + ", " + str(med) + ", " + str(max) + ", ")