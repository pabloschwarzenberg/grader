#Nota final
print("**********************")
print("Calculadora Nota Final")
print("**********************\n")

PT = float(input("Porfavor ingrese la nota de sus tareas: "))
PI = float(input("Porfavor ingrese la nota de sus interrogaciones: "))
NE = float(input("Porfavor ingrese la nota de sus examenes: "))
PP = float(input("Porfavor ingrese la nota de sus presentaciones: "))

PF = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print(" Su nota final es ", round(PF, 1))   