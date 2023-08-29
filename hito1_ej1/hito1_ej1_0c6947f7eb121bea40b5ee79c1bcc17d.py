#Nota final
pt = float(input("ingrse nuotas de la tarea: "))
pi = float(input("ingrse notas de interrogaciones: "))
ne = float(input("ingrse nota del examen: "))
pp = float(input("ingrse nota de presentacion: "))

promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
print(round(promedio,1))