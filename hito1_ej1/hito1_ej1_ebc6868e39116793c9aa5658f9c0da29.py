#Nota final
PT = float(input("Notas de las tareas: "))
PI = float(input("Notas de las interrogaciones: "))
NE = float(input("Nota del examen: "))
PP = float(input("Nota de la presentación: "))
NF = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("La nota final es: ",round(NF,1))      