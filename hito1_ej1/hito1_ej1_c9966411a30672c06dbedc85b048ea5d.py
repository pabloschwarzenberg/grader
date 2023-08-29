#Nota final
PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de la presentacion: "))
NotaFinal = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
NotaFinalRedondeada = round(NotaFinal, 1)
print("La nota final es: ",NotaFinalRedondeada )