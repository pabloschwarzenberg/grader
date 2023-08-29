#Sistema de Ecuaciones
a = int(input("Ingrese el número que acompaña a x en la primera ecuación: "))
b = int(input("Ingrese el número que acompaña a y en la primera ecuación: "))
c = int(input("Ingrese el número libre de la primera ecuación: "))
d = int(input("Ingrese el número que acompaña a x en la segunda ecuación: "))
e = int(input("Ingrese el número que acompaña a y en la segunda ecuación: "))
f = int(input("Ingrese el número libre de la segunda ecuación: "))


x = eval
y = eval



if b == e:
    x = (c - f)/(a - d)
    y = (a*f - c*d)/(b*a - b*d)

else:
    x = (e*c - b*f)/(e*a - b*d)
    y = (a*b*f - c*b*d)/(e*b*a - b*b*d)

print("Las soluciones del sistema son: X=",round(x,1),"Y=",round(y,1))

      
 