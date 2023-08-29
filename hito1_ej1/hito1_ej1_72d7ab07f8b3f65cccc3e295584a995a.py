#Nota final
NE = float(input("ingrese la nota del examen: "))
PT= float(input("ingrese la nota de tareas: "))
PI= float(input("ingrese la nota de interrogaciones: "))
PP= float(input("ingrese la nota de presentacion: "))

nota = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("su promedio final es:", round(nota,1))     