def sEcuacion(a,b,c,d,e,f):
    determinante = a*e - b*d
    if determinante != 0:
        x = (c*e - b*f)/determinante
        y = (a*f - c*d)/determinante
        
        print("x=", x, "y=", y)
    else:
        return None, None
a = int(input("Ingrese num 1:"))
b = int(input("Ingrese num 2:"))
c = int(input("Ingrese num 3:"))
d = int(input("Ingrese num 4:"))
e = int(input("Ingrese num 5:"))
f = int(input("Ingrese num 6:"))

print(sEcuacion(a,b,c,d,e,f))