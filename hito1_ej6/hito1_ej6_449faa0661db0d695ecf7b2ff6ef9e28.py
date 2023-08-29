#Ordenar tres números
num1 = int(input("Ingrese el primero numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

a = min(num1, num2, num3)
c = max(num1, num2, num3)
b = (num1 + num2 + num3) - a - c

print("{},{},{}".format(a, b, c))
     