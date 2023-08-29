#Nota final
PT = float(input("Ingresa la nota de las Tareas: "))
PI = float(input("Ingresa la nota de las Interrogaciones: "))
NE = float(input("Ingresa la nota del Examen: "))
PP = float(input("Ingresa la nota de la Presentación: "))

PromFinal = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
PromFinalRedondeado = round(PromFinal, 1)

print("El promedio final es:", PromFinalRedondeado)

