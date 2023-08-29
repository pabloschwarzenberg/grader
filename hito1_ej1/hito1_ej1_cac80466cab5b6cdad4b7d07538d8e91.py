#Nota final
pt = float(input("Ingrese la nota de las tareas: "))
pi = float(input("Ingrese la nota de las interrogaciones: "))
ne = float(input("Ingrese la nota de su examen: "))
pp = float(input("Ingrese la nota de su presentación: "))
promedio = round(0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp, 1)
print("Su promedio es: ", promedio)