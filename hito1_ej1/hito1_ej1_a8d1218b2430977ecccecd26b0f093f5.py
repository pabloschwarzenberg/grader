#Nota final
def nota_final(PT,PI,NE,PP):
    #0.3PT + 0.3PI + 0.3NE + 0.1PP
    promedio = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
    print(f"Su promedio final da {round(promedio,1)}")

#Escribir notas
tarea = float(input("Nota tareas: "))
interrogacion = float(input("Nota Interrogación: "))
examen = float(input("Nota exámen: "))
presentacion = float(input("Nota presentación: "))

nota_final(tarea,interrogacion,examen,presentacion)
 