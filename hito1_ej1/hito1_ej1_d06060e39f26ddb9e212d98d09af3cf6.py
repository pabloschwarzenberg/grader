#Nota final
PT= float(input("Ingrese nota de tareas: "))
PI= float(input("Ingrese nota de interrogaciones: "))
NE= float(input("Ingrese nota de examen: "))
PP= float(input("Ingrese nota de presentacion: "))

promedio= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

round(promedio,1)

print("El promedio es de:",promedio)
      