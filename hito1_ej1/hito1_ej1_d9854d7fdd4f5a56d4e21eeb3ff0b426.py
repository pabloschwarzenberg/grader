#Nota final
print ("calcular promedio final")   
pt = float(input("ingrese nota de tareas: "))
pi = float(input("ingrese nota de interrogaciones: "))
ne = float(input("ingrese nota de examen: "))
pp = float(input("ingrese nota de presentacion: "))

ptf = 0.3 * pt
pif = 0.3 * pi
nef = 0.3 * ne
ppf = 0.1 * pp

nf = ptf + pif + nef + ppf
nff = round (nf ,1)
print ("nota final: ",nff)