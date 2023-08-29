#Nota final
tareas = float(input("Ingrese nota tarea: "))
interrogaciones = float(input("Ingrese nota interrogacion: "))
examen = float(input("Ingrese nota examen: "))
presentacion = float(input("Ingrese nota presentacion: "))

promedio = tareas*0.3 + interrogaciones*0.3 + examen*0.3 + presentacion*0.1

print(round(promedio, 1))
