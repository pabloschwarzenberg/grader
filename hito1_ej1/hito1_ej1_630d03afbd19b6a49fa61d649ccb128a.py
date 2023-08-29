#Nota final
print("Ingrese las notas")
PT = eval(input("Ingrese la nota de las tareas: "))
PI = eval(input("ingrese la nota de las interrogaciones: "))
NE = eval(input("Ingrese la nota del examen: "))
PP = eval(input("Ingrese la nota de la presentacion: "))

P1 = 0.3 * PT
P2 = 0.3 * PI
P3 = 0.3 * NE
P4 = 0.1 * PP
PTotal = P1 + P2 + P3 + P4
round(PTotal)

print(PTotal)