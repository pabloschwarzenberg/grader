#Nota final
PT=float(input("Ingrese nota de Tareas: "))
PI=float(input("Ingrese nota de Interrogaciones: "))
NE=float(input("Ingrese nota de Examen: "))
PP=float(input("Ingrese nota de Presentacion: "))
suma=PT+PI+NE+PP
promedio=(0.3)*PT+(0.3)*PI+(0.3)*NE+(0.1)*PP
print("El promedio final de las 4 notas es:","{:.1f}".format(promedio))
