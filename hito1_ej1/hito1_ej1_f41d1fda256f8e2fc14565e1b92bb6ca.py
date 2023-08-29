#Nota final
pt=float(input("Ingrese su nota de tareas: "))
pi=float(input("Ingrese su nota de interrogaciones: "))
ne=float(input("Ingrese su nota de examen: "))
pp=float(input("Ingrese su nota de presentación: "))

prom_final=0.3*pt+0.3*pi+0.3*ne+0.1*pp

print("Su promedio final es:", round(prom_final, 1))