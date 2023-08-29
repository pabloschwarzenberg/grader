#Nota final
PT= eval(input("ingrese la nota por tareas: "))
PI= eval(input("ingrese la nota por interrogacion: "))
NE= eval(input("ingrese la nota del examen: "))
PP= eval(input("ingrese la nota por la presentacion: "))

Promedio = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
print("el promedio del alumno es:" "{0:.1f}".format(Promedio))

