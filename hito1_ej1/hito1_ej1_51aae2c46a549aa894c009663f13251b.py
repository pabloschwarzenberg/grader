#Nota final
PT = float(input("Ingrese nota tareas: "))
PI = float(input("\nIngrese nota interrogaciones: "))
NE = float(input("\nIngrese nota examen: "))
PP = float(input("\nIngrese nota presentación: "))

PF = round((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP), 1)

print("\nPromedio final:", PF)