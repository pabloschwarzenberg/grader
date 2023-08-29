#Sistema de Ecuaciones
a = int(input("INgrese un número: "))
b = int(input("INgrese un número: "))
c = int(input("INgrese un número: "))
d = int(input("INgrese un número: "))
e = int(input("INgrese un número: "))
f = int(input("INgrese un número: "))

delta = a*e - b*d
if delta !=0:
    x = (c*e - b*f) / delta
    y = (a*f - c*d) / delta
    print("x=",x,", y=",y)