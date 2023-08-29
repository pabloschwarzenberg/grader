#Nota final
PT = float(input("Ingrese el puntaje de las tareas: "))
PI = float(input("Ingrese el puntaje de las interrogaciones: "))
NE = float(input("Ingrese el puntaje del examen: "))
PP = float(input("Ingrese el puntaje de la presentación: "))

Nf = (PT + PI + NE + PP) /4

print("El promedio de notas final es: ", Nf ," ")
