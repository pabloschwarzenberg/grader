#Nota final
PT=float(input("Ingrese la nota final de sus tareas: "))
PI=float(input("Ingrese la nota final de las interrogaciones: "))
NE=float(input("Ingrese la nota final de su examen: "))
PP=float(input("Ingrese la nota final de su presentación: "))

promedioFinal=((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))
promedioFInal=float(promedioFinal)
promedioFinal=round(promedioFinal,1)
mensajeDesalida= "El promedio final de sus notas es :" + str(promedioFinal)
print(mensajeDesalida)
