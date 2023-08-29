#Nota Final
PT = float(input("Nota de tareas:"))
PI = float(input("Notas de interrogaciones: "))
NE = float(input("Notas examen: "))
PP = float(input("Notas de presentación: "))

PromedioFinal =((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))

#Promedio Final
print("El promedio final es " + str(round(PromedioFinal,1)))
