#Sistema de Ecuaciones
def solucion(a,b,c,d,e,f):
    det = a*e - b*d
    if det !=0:
        x = (c*e - b*f)/det
        y = (a*f - c*d)/det
        
        print("x=", x, "y=", y)
    else:
        return None, None
a = int(input("Ingrese numero 1:"))
b = int(input("Ingrese numero 2:"))
c = int(input("Ingrese numero 3:"))
d = int(input("Ingrese numero 4:"))
e = int(input("Ingrese numero 5:"))
f = int(input("Ingrese numero 6:"))

print(solucion(a,b,c,d,e,f))