tarea = float(input("Ingrese la nota de Tareas:  "))
interroga = float(input("Ingrese la nota de las Interrogaciones:  "))  
examen = float(input("Ingrese la nota del Examen:  "))
presenta = float(input("Ingrese la nota  de las presentaciones:  "))
resultado = tarea*0.3+interroga*0.3+examen*0.3+presenta*0.1
print("Su nota final es  " +str(round(resultado,1)))