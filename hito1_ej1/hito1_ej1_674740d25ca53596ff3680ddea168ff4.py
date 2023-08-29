#Nota final:
#Solicitar notas:    
tareas = float(input("Ingrese la nota de las tareas: ")) 
interrogaciones = float(input("Ingrese la nota de las interrogaciones: "))
examen = float(input("Ingrese la nota del examen: "))
presentacion = float(input("Ingrese la nota de la presentacion: "))
#Calcular nota final:
notafinal = (0.3*tareas + 0.3 *interrogaciones + 0.3*examen + 0.1*presentacion)
#Imprime el resultado redondeado a un decimal.    
print("La nota final es: ", round(notafinal,1))      