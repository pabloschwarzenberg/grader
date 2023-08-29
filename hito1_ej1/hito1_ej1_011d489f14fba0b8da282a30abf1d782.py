pt=float(input("ingrese la nota de tarea: "))
pi=float(input("ingrese la nota de interrogaciones: "))
ne=float(input("ingrese la nota de examen: "))
pp=float(input("ingrese la nota de su presentación: "))
promedio= 0.3*pt+0.3*pi+0.3*ne+0.1*pp
print("el promedio final de sus notas es: ",round(promedio,1))