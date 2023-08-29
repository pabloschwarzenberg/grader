num1 = int(input("Escriba el primero numero: "))
num2 = int(input("Escriba el segundo numero: "))
num3 = int(input("Escriba el tercer numero: "))

a = min(num1, num2, num3)
b = max(num1, num2, num3)
c = (num1 + num2 + num3) - a - b

print( str(a) + "," + str(c) + "," + str(b))