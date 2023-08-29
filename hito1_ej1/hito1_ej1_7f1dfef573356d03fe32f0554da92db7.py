#Nota final
PT = float(input("Tareas: "))
PI = float(input("Interrogaciones: "))
NE = float(input("Examen: "))
PP = float(input("Presentacion: "))
Nota_Final = round (0.3 * (PT + PI + NE) + 0.1 * PP, 1)
print (Nota_Final)
