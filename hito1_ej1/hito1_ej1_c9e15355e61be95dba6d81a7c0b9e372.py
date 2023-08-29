#Nota final
PT= float (input("Ingrese nota de tarea: "))
PI= float (input("Ingrese nota de interrogaciones: ")) 
NE= float (input("Ingrese nota de examen: "))
PP= float (input("Ingrese nota de presentacion: ")) 

pf= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("El promedio final de alumno es: ")
print(round(pf, 1))