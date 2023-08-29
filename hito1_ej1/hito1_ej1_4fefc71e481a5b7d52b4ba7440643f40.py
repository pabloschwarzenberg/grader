#Nota final

PT=float(input("Ingrese la nota de tarea: "))
PI=float(input("Ingrese la nota de interrogaciones: "))
NE=float(input("Ingrese la nota de examen: "))
PP=float(input("Ingrese la nota de presentacion: "))

nota_final=PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1
round(nota_final)
print("Su promedio Final de notas es:",nota_final)