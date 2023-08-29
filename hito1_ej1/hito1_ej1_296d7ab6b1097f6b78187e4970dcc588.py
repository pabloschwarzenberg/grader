#Nota final
PT=float(input("Nota tareas: "))
PI=float(input("Nota interrogaciones: "))
NE=float(input("Nota Examen: "))
PP=float(input("Nota presentacion: "))
promedio=float (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
notafinal=round (promedio,1)
print ("Su nota final es: ", notafinal)