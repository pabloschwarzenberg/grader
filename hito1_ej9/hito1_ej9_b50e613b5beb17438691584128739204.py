#Sistema de Ecuaciones

a = float(input("Ingrese valor x de la primera ecuación:"))
b = float(input("Ingrese valor y de la primera ecuación:"))
c = float(input("Ingrese valor libre de la primera ecuación:"))
d = float(input("Ingrese valor x de la segunda ecuación:"))
e = float(input("Ingrese valor y de la segunda ecuación:"))
f = float(input("Ingrese valor libre de la segunda ecuación:"))


#Se le indica al usuario que ingrese los valores de la ecuación

x=float((c-(b*((f*a)-(d*c))/((e*a)-(d*b))))/a)
y=float(((f*a)-(d*c))/((e*a)-(d*b)))


print("[x=", x,"y=",y,"]")
