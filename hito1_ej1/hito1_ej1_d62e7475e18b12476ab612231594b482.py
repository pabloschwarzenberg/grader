#Nota final
pt = float(input("Ingrese nota final de tareas: "))
pi = float(input("Ingrese nota final de las interrogaciones: "))
ne = float(input("Ingrese nota final del examen: "))
pp = float(input("Ingrese nota final de la presentacion: "))
promedio = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
promedio = round(promedio, 1)
print(promedio)




