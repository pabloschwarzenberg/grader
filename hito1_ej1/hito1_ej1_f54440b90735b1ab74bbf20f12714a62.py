#Nota final
PT = float(input("Ingrese su nota de tareas: "))
PI = float(input("Ingrese su nota de interrogaciones: "))
NE = float(input("Ingrese su nota de examen: "))
PP = float(input("Ingrese su nota de presentacion: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print(round(promedio,1))   