#Nota final
pt = float(input("Ingrese Nota de Tareas: "))
pi = float(input("Ingrese Nota de Interrogaciones: "))
ne = float(input("Ingrese Nota de Examen: "))
pp = float(input("Ingrese Nota de Presentacion: "))

promedio =(pt * 0.3 + pi * 0.3 + ne * 0.3 + pp *0.1)

print(round(promedio,1))     