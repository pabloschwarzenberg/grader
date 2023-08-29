#Nota final
pT = float(input("Ingrese su nota de Tareas: "))
pI = float(input("Ingrese su nota de Interrogaciones: "))
nE = float(input("Ingrese su nota de Examen: "))
pP = float(input("Ingrese su nota de Presentacion: "))
#Ponderacion
pt = (pT * 0.3)
pi = (pI * 0.3)
ne = (nE * 0.3)
pp = (pP * 0.1)

prom = pt + pi + ne + pp 
print("Su promedio es : ", prom)