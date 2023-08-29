#Nota final
print("Calcule su nota final")
PT = float(input("Ingrese su promedio de tareas:"))
PI = float(input("Su promedio de interrogaciones:"))
NE = float(input("Su nota de examen:"))
PP = float(input("Finalmente, su promedio se presentacion:"))
Nota_Final = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
print("Su nota final es:", Nota_Final)