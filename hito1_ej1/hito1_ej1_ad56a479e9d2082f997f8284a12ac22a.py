PP = float(input("introduce tu nota de la presentacion: "))
PI = float(input("introduce tu nota de la interrogacion: "))
PT = float(input("introduce tu nota de la tarea: "))
NE = float(input("introduce tu nota del examen: "))
PF = ((0.1 * PP) + (0.3 * PI) + (0.3 * PT) + (0.3 * NE))
print("{0:.1f}". format(PF) )