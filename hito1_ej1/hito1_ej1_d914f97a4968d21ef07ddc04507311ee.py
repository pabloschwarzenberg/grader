PT = float(input("Nota Tareas: ")) 
PI = float(input("Nota interrogaciones: "))
NE = float(input("Nota examen: ")) 
PP = float(input("Nota Presentacion: ")) 

Promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print(round(Promedio,1))