#Nota final
PT = float(input("Porfavor ingrese la nota de sus Tareas: "))
PI = float(input("Porfavor ingrese la nota de sus Interrogaciones: "))
NE = float(input("Porfavor ingrese la nota de sus Examen: "))
PP = float(input("Porfavor ingrese la nota de su Presentacion: "))

NF = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print(round(NF,1))