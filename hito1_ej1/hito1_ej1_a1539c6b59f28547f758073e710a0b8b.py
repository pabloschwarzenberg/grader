#Nota final
PT= float(input("Ingrese Nota Tarea "))
PI= float(input("Ingrese Nota Interrogación "))
NE= float(input("Ingrese Nota Examen "))
PP= float(input("Ingrese Nota Presentación "))
Promedio=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El promedio final es:" , round(Promedio, 1))