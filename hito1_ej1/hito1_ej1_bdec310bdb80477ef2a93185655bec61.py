#Nota final
PT = float(input('Tareas: '))
PI = float(input('Interrogaciones: '))
NE = float(input('Examen: '))
PP = float(input('Presemtacion: '))
promedioNotas = round(0.3*PT+ 0.3*PI+ 0.3*NE+ 0.1*PP,1)

print("El promedio de las notas es: ",promedioNotas)