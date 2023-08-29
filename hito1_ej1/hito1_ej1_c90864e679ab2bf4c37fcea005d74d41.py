#Nota final
pt = float(input("Ingresa nota de las tareas"))
pi = float(input("Ingrese nota de las interrogaciones"))
ne = float(input("Ingrese nota del examen"))
pp = float(input("ingrese nota de presentacion"))
pf = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
PF = round(pf,1)
print("tu promedio final es", PF)