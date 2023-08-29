#Calcular la nota final
pt= float(input("Ingrese la nota del item Tareas: "))
pi= float(input("Ingrese la nota del item Interrogaciones: "))
ne= float(input("Ingrese la nota del item Examen: "))
pp= float(input("Ingrese la nota del item Presentacion: "))
promedio= round ((0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp), 1)
print("Su promedio final de notas es:", promedio)   