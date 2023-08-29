#prpmedio de notas
pt=float((input("ingrese nota de tareas: ")))
pi=float(input("ingrese notas de interrogaciones: "))
ne=float(input("ingrese nota del examen: "))
pp=float(input("ingrese la nota de presentacion: "))

operatoria=round((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp),1)
print("el promedio es: ",operatoria)
