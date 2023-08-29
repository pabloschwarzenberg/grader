#Nota final
PT=float(input("ingresa la nota de tu tarea: \n"))
PI=float(input("ingresa la nota de la interrogacion: \n"))
NE=float(input("ingresa la nota del examen: \n"))
PP=float(input("ingresa la nota de la presentacion: \n"))

print("El resultado de tus notas es:","{:.1f}".format(0.3*PT+0.3*PI+0.3*NE+0.1*PP))
