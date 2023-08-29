num1 = eval(input("ingrese el primer número: "))
num2 = eval(input("ingrese el segundo número: "))
num3 = eval(input("ingrese el tercer número: "))

a = min(num1, num2, num3)
b = max(num1, num2, num3)
c = (num1 + num2 + num3) - a - b

print("Los numeros ordenados de menor a mayor son: ", a,",",c,",", b)