def sistecuaciones(a, b, c, d, e, f):
    formula = a*e-b*d

    if formula != 0:
        x=(c*e-b*f)/formula
        y=(a*f-c*d)/formula
        print("x=",x)
        print("y=",y)
    else:
        print("no se puede resolver")

print("Ingrese valores para: a, b, c, d, e y f:")
a= int(input("Ingrese valor a: "))
b= int(input("Ingrese valor b: "))
c= int(input("Ingrese valor c: "))
d= int(input("Ingrese valor d: "))
e= int(input("Ingrese valor e: "))
f= int(input("Ingrese valor f: "))

print(sistecuaciones(a, b, c, d, e, f))