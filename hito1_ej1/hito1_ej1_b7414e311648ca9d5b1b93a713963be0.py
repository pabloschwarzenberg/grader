pt = float(input("Ingrese las notas de las tareas: "))
pi = float(input("Ingrese las notas de las interrogaciones: "))
ne = float(input("Ingrese la nota del examen: "))
pp = float(input("Ingrese la nota de la presentacion: "))

prom_final = (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

print("El promedio es: ", round (prom_final,1))
