#nota final
PT = float(input("nota de tareas: "))
PI = float(input("nota de interrogaciones: "))
NE = float(input("nota de examen: "))
PP = float(input("nota de presentacion: "))
final = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("{0:.1f}".format(final))