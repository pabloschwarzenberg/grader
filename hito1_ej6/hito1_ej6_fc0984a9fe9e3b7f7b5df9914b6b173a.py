#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

a = min(num1 , num2 , num3)
c = max(num1 , num2 , num3)
b = (num1 + num2 + num3) - a - c

print(str(a)+","+str(b)+","+str(c))