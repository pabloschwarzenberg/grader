num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

a = min(num1, num2, num3)
c = max(num1, num2, num3)
b = (num1 + num2 + num3) - a - c 

print("Los numeros ordenados son: {},{},{}".format(a, b, c))