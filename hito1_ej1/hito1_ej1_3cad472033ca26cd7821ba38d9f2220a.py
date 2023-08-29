#Nota final
PT = float(input("Introduzca la nota de las Tareas: "))
PI = float(input("Introduzca la nota de las interrogaciones: "))
NE = float(input("Introduzca la nota del Examen: "))
PP = float(input("Introduzca la nota de la Presentación: "))

PromedioFinal = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print ("El promedio Final es de: ", round (PromedioFinal, 1))

      