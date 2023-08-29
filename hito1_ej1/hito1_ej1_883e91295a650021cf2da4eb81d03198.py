#Nota final
PT = input ("Ingrese nota de Tareas: ")
PI = input ("Ingrese nota de Interrogaciones: ")
NE = input ("Ingrese nota de Examen: ")
PP = input ("Ingrese nota de Presentación: ")

promedioFinal = (0.3*float (PT))+(0.3*float (PI))+(0.3*float (NE))+(0.1*float (PP))

print ("Su promedio final es: ", round (promedioFinal, 1))      