def soluciones(a,b,c,d,e,f):
    det = a*e - b*d
    if det !=0:
        x = (c*e - b*f)/det
        y = (a*f - c*d)/det
        
        print("x=", x, "y=", y)
    else:
        return None, None
a = int(input("Ingrese digito 1:"))
b = int(input("Ingrese digito 2:"))
c = int(input("Ingrese digito 3:"))
d = int(input("Ingrese digito 4:"))
e = int(input("Ingrese digito 5:"))
f = int(input("Ingrese digito 6:"))

print(soluciones(a,b,c,d,e,f))
