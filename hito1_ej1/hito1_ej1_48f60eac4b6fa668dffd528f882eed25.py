#Nota final
notas = [0,0,0,0]
notas[0] = float(input(" ingrese la nota de las tareas: "))
notas[1] = float(input(" ingrese la nota de las interrogaciones: "))
notas[2] = float(input(" ingrese la nota del examen: "))
notas[3] = float(input(" ingrese la nota de la presentacion: "))

promedioF = (notas[0] * 0.3) + (notas[1] * 0.3) + (notas[2] * 0.3) + (notas[3] * 0.1)
promedioF = round(promedioF, 1)
print(promedioF)     