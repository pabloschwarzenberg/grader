#Sistema de Ecuaciones
print("Introducir coeficientes numéricos de la primera ecuación de la forma ax+by=c")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
print("Introducir coeficientes numéricos de la segunda ecuacion de la forma dx+ey=f")
d=int(input("d="))
e=int(input("e="))
f=int(input("f="))
#la solución puede ser un número real, por lo que no debieras usar la división entera
x = ((b*f)-(c*e)) / ((b*d)-(a*e))
y = ((a*f)-(c*d)) / ((a*e)-(b*d))
#el programa que revisa espera un decimal en el resultado, o sea hay que redondear:
print("x="+str(round(x,1)))
print("y="+str(round(y,1)))