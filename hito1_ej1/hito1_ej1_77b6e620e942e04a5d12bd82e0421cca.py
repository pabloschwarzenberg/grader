#Nota final
pt=float(input("nota tareas: "))
pi=float(input("nota interrogaciones: "))
ne=float(input("nota examen: "))
pp=float(input("presentacion: "))
R=0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
resultado=round(R, 1)
print(resultado)