#Nota final
PT = float(input("ingrese nota de tareas: ")) * 0.3
PI = float(input("ingrese nota de interrogaciones: ")) * 0.3
NE = float(input("ingrese nota de examen: ")) * 0.3
PP = float(input("ingrese nota de presentacion: ")) * 0.1

nf = (PT + PI + NE + PP)
print("{:.1f}".format(nf)) 