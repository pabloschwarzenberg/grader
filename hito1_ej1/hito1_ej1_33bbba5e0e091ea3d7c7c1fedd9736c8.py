#Nota final
 #Entradas

PT = float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE = float(input("Ingrese nota de examen: "))
PP = float(input("Ingrese nota de presentación: "))

#Procedimiento

PF = round(((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)), 1)

#Salida

print("El promedio final es: ",PF)     