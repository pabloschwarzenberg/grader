#Nota final
PT = float(input("Ingrese el Promedio de notas de las Tareas: " ))
PI = float(input("Ingrese el Promedio de notas de las Interrogaciones: " ))
NE = float(input("Ingrese la Nota del Examen: " ))
PP = float(input("Ingrese el Promedio de las Presentaciones: " ))

Promedio = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)

print( "Promedio Final es", round (Promedio,1))
 