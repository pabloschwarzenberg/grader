#Nota final
Tareas = float(input("inserte su nota de tareas:"))
Interrogaciones = float(input("inserte su nota de interrogaciones:"))
Examen = float(input("inserte su nota de examen:"))
Presentacion = float(input("inserte su nota de presentacion:"))

Promedio = float(0.3 * Tareas + 0.3 * Interrogaciones + 0.3 * Examen + 0.1 * Presentacion)

print(Promedio)