#Nota final
tarea = float(input("ingrese calificacion de la tarea:"))
interrogacion = float(input("ingrese calificacion de la interrogacion:"))
examen = float(input("ingrese calificacion del examen:"))
presentacion = float(input("ingrese calificacion de la presentacion:"))
promedio = ((tarea * 0.3)+(interrogacion * 0.3)+(examen * 0.3)+(presentacion * 0.1))
print("promedio final:", promedio)