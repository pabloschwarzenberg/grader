#Nota final
NT = float(input("Ingrese La Nota De Tareas: "))
NI = float(input("Ingrese La Nota De Interrogación: "))
NE= float(input("Ingrese La Nota Del Examen: "))
NP =float(input("Ingrese La Nota De Presentacion: "))
promedio=0.3*NT + 0.3*NI + 0.3*NE + 0.1*NP
print("Su Promedio De Notas Es De: ",round(promedio,1))      