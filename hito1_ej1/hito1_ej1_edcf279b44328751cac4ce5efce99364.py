#Nota final
#PT = Tareas
#PI = Interrogaciones 
#NE = Examen
#PP = Presentacion
# formula 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprimir el resultado redondiado a un decimal.
PT= float(input("ingrese nota de tareas: "))
PI= float(input("ingrese nota de interrogaciones: "))
NE= float(input("ingrese nota del examen: "))
PP= float(input("ingrese nota de participacion: "))
promedio_final= (PT *0.3) + (PI *0.3) + (NE *0.3) +(PP *0.1)
redondear=round (promedio_final,1)
print("la nota final es: " + str (redondear))