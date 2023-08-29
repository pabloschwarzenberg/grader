#Nota final
print("NOTAS")

PT = float(input("Tareas:"))
PI = float(input("interrogaciones:"))
NE = float(input("Examen:"))
PP = float(input("Presentacion:"))

Promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print("Su promedio es",(round(Promedio, 1)))   