#Nota final
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
print("Calculador de notas")
PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota de examen: "))
PP = float(input("Ingrese la nota de presentacion: "))
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
print("Promedio final: ", round(promedio,1))      