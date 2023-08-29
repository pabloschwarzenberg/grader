pt = float(input("Ingrese nota de tarea "))
pi = float(input("Ingrese nota de interrigacion "))
ne = float(input("Ingrese nora de examen "))
pp = float(input("Ingrese nota de presentacion "))

pt = float(pt * 0.3)
pi = float(pi * 0.3)
ne = float(ne * 0.3)
pp = float(pp * 0.1)

nf = pt + pi + ne + pp
print("Su promedio final es ",nf)