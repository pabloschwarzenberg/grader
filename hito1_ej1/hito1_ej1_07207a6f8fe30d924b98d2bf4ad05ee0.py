#Nota final
PT=eval(input("Ingrese la nota de sus tareas: "))
PI=eval(input("ingrese la nota de sus interrogaciones: "))
NE=eval(input("ingrese la nota del examen: "))
PP=eval(input("ingrese la nota de la presentación: "))

notafinal= (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print(round(notafinal,1))