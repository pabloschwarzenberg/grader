#Nota final

PT = float(input("Ingresar nota de tareas: "))
PI = float(input("Ingresar nota de interrogaciones: "))
NE = float(input("Ingresar nota de Examen: "))
PP = float(input("Ingresar nota de Presentacion: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(promedio)
redondeo = round(promedio, 1)
print(redondeo)