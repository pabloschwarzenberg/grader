#Sistema de Ecuaciones
def sistema_de_ecuaciones(a, b, c, d, e, f):
    discriminante = a*e - b*d
    if discriminante != 0:
        x = (c*e - b*f)/discriminante
        y = (a*f - c*d)/discriminante
    print("x=",x)
    print("y=",y)
    
a = int(input("Ingrese numero a: "))
b = int(input("Ingrese numero b: "))
c = int(input("Ingrese numero c: "))
d = int(input("Ingrese numero d: "))
e = int(input("Ingrese numero e: "))
f = int(input("Ingrese numero f: "))

print(sistema_de_ecuaciones(a, b, c, d, e, f))