#Nota final
PT= float(input("Ingresa nota Tareas: "))
PI= float(input("Ingresa nota Interrogaciones: "))
NE= float(input("Ingresa nota Examen: "))
PP= float(input("Ingresa nota Presentacion: "))

nota_final=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("La nota final del curso es: ", round(nota_final, 1))