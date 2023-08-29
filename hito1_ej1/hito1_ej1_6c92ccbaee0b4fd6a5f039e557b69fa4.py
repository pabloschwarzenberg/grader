#Nota Final
PT = float(input("Ingrese nota de su tarea"))
PI = float(input("Ingrese nota de su interrogaciones"))
NE = float(input("Ingrese nota de su examen"))
PP = float(input("Ingrese nota de su presentacion"))
Nota = round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1)
print(Nota)