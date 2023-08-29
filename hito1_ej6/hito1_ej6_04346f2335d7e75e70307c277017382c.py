#Ordenar tres números
num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba el segundo numero: "))
num3 = int(input("Escriba el tercer numero: "))
a = min(num1, num2, num3)
b = max(num1, num2, num3)
c = (num1 + num2 + num3) - a - b
print("Los numeros ordenados son: {}, {}, {}".format(a, b, c))