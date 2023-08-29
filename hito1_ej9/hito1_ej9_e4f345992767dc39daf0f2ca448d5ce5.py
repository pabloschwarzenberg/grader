#Sistema de Ecuaciones
def solucion(a,b,c,d,e,f):
    det = a*e - b*d
    if det !=0:
        x = (c*e - b*f)/det
        y = (a*f - c*d)/det

        print("x=", x, "y=", y)
    else:
        return None, None
a = int(input("Ingrese el 1mer número:"))
b = int(input("Ingrese el 2do número:"))
c = int(input("Ingrese el 3cer número:"))
d = int(input("Ingrese el 4to número:"))
e = int(input("Ingrese el 5to número:"))
f = int(input("Ingrese el 6to número:"))
print(solucion(a,b,c,d,e,f))      