#Nota final
tareas = eval(input("Ingrese nota de tareas: "))

interrogaciones = eval(input("Ingrese nota de la interrogacion: "))

examen = eval(input("Ingrese nota del examen: "))

presentacion = eval(input("Ingrese nota de presentacion: "))


nota = 0.3*tareas+0.3*interrogaciones+0.3*examen+0.1*presentacion

print("La nota es", nota)