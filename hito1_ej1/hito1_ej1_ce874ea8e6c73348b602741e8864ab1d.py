#Nota final

PT = float(input('Digite la nora de Tareas: '))
PI = float(input('Digite la nora de Interrogaciones: '))
NE = float(input('Digite la nora de Examen: '))
PP = float(input('Digite la nora de Presentacion: '))

NF = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print(round(NF, 2))