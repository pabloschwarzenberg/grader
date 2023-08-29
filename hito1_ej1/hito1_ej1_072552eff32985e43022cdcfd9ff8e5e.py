#Nota final
pt=float(input("Introduzca promedio de tareas: "))
pi=float(input("Introduzca promedio de interrogaciones: "))
ne=float(input("Introduzca nota de examen: "))
pp=float(input("Introduzca promedio de presentación: "))
NotaFinal=0.3*pt+0.3*pi+0.3*ne+0.1*pp
Nota=round(NotaFinal,1)
print(Nota)
      