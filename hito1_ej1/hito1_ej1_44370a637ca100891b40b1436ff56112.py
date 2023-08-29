#Nota final
PT = int(input("Ingrese nota tareas: "))
PI = int(input("Ingrese nota interrogaciones: "))
NE = int(input("Ingrese nota examen: "))
PP = int(input("Ingrese nota presentacion: "))
PTF = 0.3 * PT
PIF = 0.3 * PI
NEF = 0.3 * NE
PPF = 0.1 * PP
PF = (PTF+PIF+NEF+PPF) / 4
print(PF)