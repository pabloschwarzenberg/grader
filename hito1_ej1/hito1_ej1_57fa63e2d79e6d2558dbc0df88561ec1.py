#Nota final
print("ingrese notas de tarea")
pt=float(input())
print("ingrese notas interrogaciones")
pi=float(input())
print("ingrese nota de examen")
ne=float(input())
print("ingrese nota de presentacion")
pp=float(input())

nota=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

nota_final=round(nota,1)

print("la nota final es:", nota_final)