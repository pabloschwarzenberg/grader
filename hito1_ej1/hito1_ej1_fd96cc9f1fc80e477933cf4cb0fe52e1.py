#Nota final
PT= float(input("ingresar nota tarea: "))
PI= float(input("ingresar nota interrogacion: "))
NE= float(input("ingresar nota examen: "))
PP= float(input("ingresar nota presentacion: "))

promedio= 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
redondeado= round(promedio, 1)
print("promedio final: ", redondeado)      