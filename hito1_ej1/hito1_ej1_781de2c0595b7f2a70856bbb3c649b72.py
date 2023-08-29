#Nota final
print("Ingrese sus cuatro notas porfavor :")
Tareas = float(input("Su nota en tareas es de: "))
Interrogaciones = float(input("Su nota en interrogaciones es de: "))
Examen = float(input("Su nota en examen es de: "))
Presentacion = float(input("Su nota en presentacion es de: "))
x = ((0.3*Tareas + 0.3*Interrogaciones + 0.3*Examen + 0.1*Presentacion))
x = round(x,1)
print("El promedio que ingreso redondeado es de :", x)