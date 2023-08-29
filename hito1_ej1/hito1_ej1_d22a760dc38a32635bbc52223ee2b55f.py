#Nota final
pt = float(input("ingrese el promedio de trabajos: "))
pi = float(input("ingrese el promedio de interrogaciones: "))
ne = float(input("ingrese nota de examen: "))
pp = float(input("ingrese promedio de presentacion: "))

pf = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
print("el promedio final es:",round(pf,1))  