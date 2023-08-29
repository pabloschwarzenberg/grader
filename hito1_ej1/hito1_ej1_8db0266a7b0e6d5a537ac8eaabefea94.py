#Nota final
pt = int(input("Ingrese nota de tareas: "))
pin = int(input("Ingrese nota de interrogaciones: "))
ne = int(input("Ingrese nota de examen: "))
pp = int(input("Ingrese nota de presentación: "))

promedio = 0.3*pt * 0.3*pin + 0.3*ne + 0.1*pp
promedio_final = round(promedio,1)

print(promedio_final)