#Nota final
#Entrada
PT=float(input("Introduzca la nota de las tareas: "))
PI=float(input("Introduzca la nota de las interrogaciones: "))
NE=float(input("Introduzca la nota del examen: "))
PP=float(input("Introduzca la nota de la nota de la presentación: "))

promedio=((0.3*PT) + (0.3*PI) + (0.3*NE) +(0.1*PP))
promedio=round(promedio,1)
print(promedio)
      