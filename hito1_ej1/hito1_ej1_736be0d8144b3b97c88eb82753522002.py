#Nota final
PT = eval(input("ingrese la nota de su tarea: "))
PI = eval(input("ingrese la nota de su interrogaciones: "))
NE = eval(input("ingrese la nota de su examen: "))
PP = eval(input("ingrese la nota de su presentacion: "))

PM = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
PM = round(PM,1)
print("el promedio de las notas es: ", PM)