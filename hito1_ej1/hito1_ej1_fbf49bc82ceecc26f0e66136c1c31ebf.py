#Nota final
PT = float(input("ingrese nota tareas"))
PI = float(input("ingrese nota interogaciones"))
NE = float(input("ingrese nota examen"))
PP = float(input("ingrese nota Preentacion"))

NF = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print("tu nota final es:", NF)
