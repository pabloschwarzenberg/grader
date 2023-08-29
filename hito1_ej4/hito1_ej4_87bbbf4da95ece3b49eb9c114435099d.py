a = int(input("Ingresa un número decimal: "))
b = ""

while a > 0:
    resto = int(a % 2)
    a = int(a / 2)
    b = str(resto) + b
print("resultado=", b)