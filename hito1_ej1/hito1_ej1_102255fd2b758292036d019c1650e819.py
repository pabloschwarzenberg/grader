#Nota final
pt=float(input( "ingrese su nota de tarea: "))
pi=float(input( "ingrese su nota de interrogacion: "))
ne=float(input( "ingrese su nota de examen: "))
pp=float(input( "ingrese su nota de presentacion: "))

promedio = ((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (pp * 0.1))

print("su promedio final es: ", round(promedio, 1 ))