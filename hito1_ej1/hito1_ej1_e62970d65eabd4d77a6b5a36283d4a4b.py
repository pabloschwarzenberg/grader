pt = float(input("Ingrese la nota de tareas"))
pi = float(input("Ingrese la nota de interrogaciones"))
ne = float(input("Ingrese la nota del exámen"))
pp = float(input("Ingrese la nota de presentación"))

notaFinal = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
notaFinal = round(notaFinal,1)

print(notaFinal)