#Realiza un programa para preguntar al usuario cuatro notas
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprime el resultado redondeado a un decimal.
from os import system
system ("cls")

PT = float(input("Ingrese nota Tareas: "))
PI = float(input("Ingrese nota Interrogaciones: "))
NE = float(input("Ingrese nota Examen: "))
PP = float(input("Ingrese nota Presentacion: "))

PT2 = (PT /100) * 30
PI2 = (PI /100) * 30
NE2 = (NE /100) * 30
PP2 = (PP /100) * 10

resultado = PT2 + PI2 + PP2 + NE2

#la actividad no acepta codigos que tengan un print escrito asi: print(f"Su promedio es de: {resultado:.1f}")
promedio_redondeado = round(resultado, 1)

print("Su promedio es de:", promedio_redondeado)