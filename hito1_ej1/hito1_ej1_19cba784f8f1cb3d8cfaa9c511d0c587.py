#Nota final
PT = float(input("Nota Tareas: "))
PI = float(input("Nota Interrogaciones: "))
NE = float(input("Nota Examen: "))
PP = float(input("Nota Presentacion: "))
Promedio = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print ("{}".format(round(Promedio, 1)))