#Nota final
PT = float(input("Ingrese el/las notas que tiene en tareas --> "))
PI = float(input("Ingrese el/las notas que tiene en interrogaciones --> "))
NE = float(input("Ingrese el la nota del examen --> "))
PP = float(input("Ingrese la nota de presentacion que tiene --> "))

final = round((0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP),1)
print("El promedio entre las tareas, interrogaciones, el/los examen(es) y la presentacion fue de -->",final)   