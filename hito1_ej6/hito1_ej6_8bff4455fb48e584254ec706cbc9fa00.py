#Ordenar tres números
num1= input("Introduce el primer número")
num2= input("Introduce el segundo número")
num3= input("Introduce el tercer número")

a = min(num1, num2, num3)
b = max(num1, num2, num3)
c = (num1 + num2 + num3) - a - b

print(f" {a}, {c}, {b} ")