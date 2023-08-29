#Nota final
#PT = Tareas
#PI = Interrogaciones
#NE = Examen
#PP = Presentacion
#PF = Promedio Final

#Entrada de datos
PT = float(input("Ingrese la nota por Tareas: "))
PI = float(input("Ingrese la nota por Interrogaciones: "))
NE = float(input("Ingrese la nota por Examen: "))
PP = float(input("Ingrese la nota por Presentacion: "))
PF = 0
#Procesamiento de datos
PF = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
PF = round (PF,1)
#Salida de datos
print("Su promedio final es:", PF)