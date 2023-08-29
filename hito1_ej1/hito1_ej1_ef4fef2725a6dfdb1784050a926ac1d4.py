#Nota final
PT=float(input("Ingrese notas de las tareas:"))
PI=float(input("Ingrese notas por interrogacion: "))
NE=float(input("Ingrese notas del examen: "))
PP=float(input("Ingrese notas de presentacion: "))
promedio=round((0.3*PT+0.3*PI+0.3*NE+0.1*PP),1)
print("Su promedio es : ",promedio)
     