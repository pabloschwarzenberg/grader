NT = "nota"
PT = "Tareas"
PI = "Interrogaciones"
NE = "Examen"
PP = "Presentacion"
NT = float(input("Notas"))
PT = float(input("Tareas"))    
PI = float(input("Interrogaciones"))
NE = float(input("Examen"))
PP = float(input("Presentacion:"))
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP 
print(format(promedio, '0.1f'))