#Nota final
tareas=float(input("Ingrese la nota de su tarea: "))
interrogaciones=float(input("Ingrese la nota de su interrogacion: "))
examen=float(input("Ingrese la nota de su examen: "))
presentacion= float(input("Ingrese la nota de presentacion: "))
promedio= 0.3*tareas+0.3*interrogaciones+0.3*examen+0.1*presentacion
promedior=round(promedio,1)
print(promedior)