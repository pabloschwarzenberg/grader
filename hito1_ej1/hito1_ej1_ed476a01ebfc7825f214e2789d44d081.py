#Nota final

#Entrada

PT = float(input("Notas tareas: "))
PI = float(input("Notas interrogaciones: "))
NE = float(input("Notas exámen: "))
PP = float(input("Notas presentación: "))

#Evaluación

notaFinal = PI*0.3 + PT*0.3 + NE*0.3 + PP*0.1
round(notaFinal,1)

print("Promedio: ", notaFinal)