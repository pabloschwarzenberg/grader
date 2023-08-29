#Nota final
pt = float(input("introduzca nota de Tareas" ))
pi = float(input("introduzca nota de Interrogaciones" ))
ne = float(input("introduzca nota de Examen "))
pp = float(input("introduzca nota de Presentacion"))
print("Su nota final es", round((0.3*(pt + pi + ne) + 0.1*pp),1))