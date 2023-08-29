#Nota final
      
      
PT = float(input("Ingrese la nota de las Tareas: "))
PI = float(input("Ingrese la nota de las Interrogaciones: "))
NE = float(input("Ingrese la nota del Examen: "))
PP = float(input("Ingrese la nota de la presentacion: "))
promedio = 0.3*PT+0.3*PI+0.3*NE+0.1*PP

print("La nota final es: " + str(round(promedio,1)))
