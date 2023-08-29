# ax + by = c
# dx + ey = f

a =float(input("Ingrese a: "))
b =float(input("Ingrese b: "))
c =float(input("Ingrese c: "))
d =float(input("Ingrese d: "))
e =float(input("Ingrese e: "))
f =float(input("Ingrese f: "))

determinante = float ((a * e)- (b * d))

if determinante !=0:
    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante

    print("x=" + str(x))
    print("y=" + str(y))






