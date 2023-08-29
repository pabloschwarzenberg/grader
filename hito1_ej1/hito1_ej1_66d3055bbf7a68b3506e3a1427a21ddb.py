#Nota final
pt=float(input("Ingrese la nota final de tareas: "))
pi=float(input("Ingrese la nota final de interrogaciones: "))
ne=float(input("INgrese nota final de examen: "))
pp=float(input("Ingrese nota final de presentación: "))

nt= 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
print("La nota final es: " + str(nt))