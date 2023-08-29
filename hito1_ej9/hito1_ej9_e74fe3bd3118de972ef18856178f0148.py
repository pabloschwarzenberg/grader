a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))
c = int(input("Ingrese un número: "))
d = int(input("Ingrese un número: "))
e = int(input("Ingrese un número: "))
f = int(input("Ingrese un número: "))

k = a*e - b*d

if k != 0:
    x = (c*e - b*f) / k
    y = (a*f - c*d) / k
    print("x=",x, ",", "y=",y)
    