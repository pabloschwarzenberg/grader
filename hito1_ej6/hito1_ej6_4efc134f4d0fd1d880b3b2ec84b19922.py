#Ordenar tres números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a <= b and a <= c:
    if b <= c:
        print(a, b, c, sep=",")
    else:
        print(a, c, b, sep=",")
elif b <= a and b <= c:
    if a <= c:
        print(b, a, c, sep=",")
    else:
        print(b, c, a, sep=",")
else:
    if a <= b:
        print(c, a, b, sep=",")
    else:
        print(c, b, a, sep=",")