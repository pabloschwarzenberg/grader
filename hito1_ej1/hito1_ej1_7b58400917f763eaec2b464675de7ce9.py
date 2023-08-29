#Nota final
PT=float (input("Ingrese notas de tareas del alumno:"))
PI=float (input("Ingrese notas de interrogaciones del alumno:"))
NE=float (input("Ingrese notas de examen del alumno:"))
PP=float (input("Ingrese nota de presentación del alumno:"))


NF= (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print ("Promedio final del alumno es:", NF)     