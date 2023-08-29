#Nota final
PT = float(input("Ingrese nota promedio de las tareas: "))
PI = float(input("Ingrese nota promedio de las interrogaciones: "))
NE = float(input("Ingrese nota del examen: "))
PP = float(input("Ingrese  nota de la presentación: "))
promedioFinal = 0.3*(PT) + 0.3*(PI) + 0.3*(NE) + 0.1*(PP)
round(promedioFinal, 1)
print("Su promedio final es", promedioFinal)
   