#Sistema de ecuaciones

print("Resolviendo sistema de ecuaciones * ax+by=c  dx+ey=f *")
a = float(input("Ingrese valor para a: "))
b = float(input("Ingrese valor para b: "))
c = float(input("Ingrese valor para c: "))
d = float(input("Ingrese valor para d: "))
e = float(input("Ingrese valor para e: "))
f = float(input("Ingrese valor para f: "))


de = a*e - b*d

if de != 0:
    x = (c*e - b*f) / de
    y = (a*f - c*d) / de
    print("['x=",x,"','y=",y,"']")
else:
    print("No existe solución para x e y")
