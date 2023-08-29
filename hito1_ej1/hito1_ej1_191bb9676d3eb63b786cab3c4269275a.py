#Nota final
#PT= Tareas
#PI= Interrogaciones
#NE= Examen
#PP= Presentación
#promedio= 0.3*PT + 0.3*PI + 0.3* NE + 0.1*PP

PT=float(input("Escriba su nota de tareas: " ))
PI=float(input("Escriba su nota de interrogaciones: "))
NE=float(input("Escriba su nota del examen: "))
PP=float(input("Escriba su nota de presentacion: "))

print ("El promedio corresponde a: ", round(0.3*PT + 0.3*PI + 0.3* NE + 0.1*PP,1) )
     