#Nota final
PT=float(input("ingrese la nota de tarea: "))
PI=float(input("ingrese nota de interogante: "))
NE=float(input("ingrese nota de examen: "))
PP=float(input("ingrese nota de presentacion: "))

promedioF=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("el resultado es: ",round(promedioF,1))