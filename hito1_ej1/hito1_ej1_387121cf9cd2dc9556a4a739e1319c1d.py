#Nota final
def calcular_promedio():
    PT = float(input("Ingrese la nota de Tareas: "))
    PI = float(input("Ingrese la nota de Interrogaciones: "))
    NE = float(input("Ingrese la nota del Examen: "))
    PP = float(input("Ingrese la nota de Presentación: "))
    
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    promedio_redo = round(promedio, 1)
    print("Su promedio final es de:", promedio_redo)
calcular_promedio()