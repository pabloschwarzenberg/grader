#Sebastian hintermann
pt=float(input("ingrese su nota de tareas"))
pi=float(input("ingrese su nota de interrogaciones"))
ne=float(input("ingrese su nota de examen"))
pp=float(input("ingrese su nota de presentacion"))
n1=0.3*pt
n2=0.3*pi
n3=0.3*ne
n4=0.1*pp
notafinal=round(n1+n2+n3+n4,1)

print("el resultado final es:",notafinal)