#Nota final

PT = float(input("Ingrese nota de las Tareas:"))

PI = float(input("Ingrese nota de las Interrogaciones:"))

NE = float(input("Ingrese nota del Examen:"))

PP = float(input("Ingrese nota de la presentación:"))

PromedioFinal = ((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP))

print("{0:.1f}".format(PromedioFinal))