#Nota final
PT = float(input("Ingrese la nota de las tareas: "))    
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de la presentacion: "))
PROMEDIO = float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("Su promedio final es:", round(PROMEDIO,1))
