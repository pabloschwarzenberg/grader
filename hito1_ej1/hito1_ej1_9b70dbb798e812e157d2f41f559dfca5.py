#Nota final
pt=float(input("escriba su promedio en tareas: "))
pi=float(input("escriba su promedio en interrogaciones: "))
ne=float(input("escriba su nota de examen: "))
pp=float(input("escriba su nota de presentacion al examen: "))
nf=0.3*pt+0.3*pi+0.3*ne+0.1*pp
f=round(nf,1)
print("su promedio final es: ",f)