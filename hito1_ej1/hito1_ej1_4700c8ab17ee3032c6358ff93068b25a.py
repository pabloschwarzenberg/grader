#Nota final
print("Ingrese los promedios correspondientes a sus calificaciones")

pt = float(input("Promedio Tareas: "))
pi = float(input("Promedio Interrogaciones: "))
ne = float(input("Nota Examen: "))
pp = float(input("Presentación: "))

p =0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print("Su promedio es: ",round(p,1))