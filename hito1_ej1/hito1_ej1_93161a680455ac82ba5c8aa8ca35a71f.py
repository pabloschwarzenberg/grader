#Nota final
A=float(input("Ingrese la nota de su tarea: "))
B=float(input("Ingrese la nota de su interrogación: "))
C=float(input("Ingrese la nota de su examen: "))
D=float(input("Ingrese la nota de su presentación: "))
promedio=round((0.3*A + 0.3*B + 0.3*C + 0.1*D)**1,1)
print(promedio)