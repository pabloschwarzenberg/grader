#Nota final

PT = float(input("Ingrese nota de Tareas: "))
PI = float(input("Ingrese nota de Interrogantes: "))
NE = float(input("Ingrese nota de Examen: "))
PP = float(input("Ingrese nota de Presentacion: "))
      
Promedio = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
pfinal = (Promedio//1) + (Promedio%1)
print("El promedio final es: ",pfinal)