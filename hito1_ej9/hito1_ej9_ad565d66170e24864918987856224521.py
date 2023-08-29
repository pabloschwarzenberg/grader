#Sistema de Ecuaciones
def solucion(a,b,c,d,e,f):
    det = a*e - b*d
    if det !=0:
        x = (c*e - b*f)/det
        y = (a*f - c*d)/det
        
        print("x=", x, "y=", y)
    else:
        return None, None
a = int(input("Ingrese el primer numero :"))
b = int(input("Ingrese el segundo numero:"))
c = int(input("Ingrese el tercer numero:"))
d = int(input("Ingrese el cuarto numero:"))
e = int(input("Ingrese el quinto numero:"))
f = int(input("Ingrese el sexto numero:"))

print(solucion(a,b,c,d,e,f))      