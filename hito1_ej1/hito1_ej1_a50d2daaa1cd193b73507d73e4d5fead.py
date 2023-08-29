#Nota final
PT=float(input("Ingrese la nota de Tareas: "))*0.3
PI=float(input("Ingrese la nota de Interrogaciones: "))*0.3
NE=float(input("Ingrese la nota de Examen: "))*0.3
PP=float(input("Ingrese la nota de Presentación: "))*0.1
NF=PT+PI+NE+PP
NF=NF.__round__(1)
print("La Nota Final sería:",NF)