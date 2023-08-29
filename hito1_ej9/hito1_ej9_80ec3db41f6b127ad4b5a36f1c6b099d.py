#Sistema de Ecuaciones

def solucion(a,b,c,d,e,f):
    det = a*e - b*d
    if det !=0:
        x = (c*e - b*f)/det
        y = (a*f - c*d)/det
        
        print("x=", x, "y=", y)
    else:
        return None, None
a = int(input("Ingrese el primer número:"))
b = int(input("Ingrese el segundo número:"))
c = int(input("Ingrese el tercer número:"))
d = int(input("Ingrese el cuarto número:"))
e = int(input("Ingrese el quinto número:"))
f = int(input("Ingrese el sexto número:"))

print(solucion(a,b,c,d,e,f))