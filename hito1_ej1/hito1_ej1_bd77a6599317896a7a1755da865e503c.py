#Nota final

#tareas = 30%
#interrogaciones = 30%
#examen = 30%
#presentacion = 10%


tareas = float(input("Ingrese la nota del tarea: "))
interrogacion = float(input("Ingrese la nota de interrogacion: "))
examen = float(input("Ingrese la nota de examen: "))
presentacion = float(input("Ingrese la nota de presenyacion: "))

nota = (tareas*0,3 + interrogacion*0.3 + examen*0,3 + presentacion*0,1)

print("la ota definitiva del estudiante es: " , nota)
