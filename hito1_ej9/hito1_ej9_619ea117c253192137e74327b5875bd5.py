#Sistema de Ecuaciones
def solucion_sistema_ecuaciones(a, b, c, d, e, f):
    formula = a*e-b*d

    if formula != 0:
        x=(c*e-b*f)/formula
        y=(a*f-c*d)/formula
        print("x=",x)
        print("y=",y)
    else:
        print("no se puede resolver")

print("ingrese los valores para a, b, c, d, e y f:")
a=int(input("ingrese el primer numero:"))
b=int(input("ingrese el segundo numero"))
c=int(input("ingrese el tercer numero"))
d=int(input("ingrese el cuarto numero"))
e=int(input("ingrese el quinto numero"))
f=int(input("ingrese el sexto numero"))
print(solucion_sistema_ecuaciones(a, b, c, d, e, f))