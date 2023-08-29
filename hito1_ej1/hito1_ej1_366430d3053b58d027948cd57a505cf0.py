#Nota final
# Entrada
PT = float(input("Nota de tareas: "))
PI = float(input("Nota de interrogaciones: "))
NE = float(input("Nota de examenes: "))
PP = float(input("Nota de presentaciones: "))

# Proceso
promedio= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
promedio= round(promedio, 1)

# Salida
print("El promedio de notas es: ", promedio)   