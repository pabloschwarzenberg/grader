#Nota final
pt=float(input("Ingrese nota de tareas: "))
pi=float(input("Ingrese nota de interrogaciones: "))
ne=float(input("Ingrese nota de exámen: "))
pp=float(input("Ingrese nota de presentación: "))
f=0.3*pt+0.3*pi+0.3*ne+0.1*pp
fr=round(f,1)
print("Su promedio final es:",fr)
      