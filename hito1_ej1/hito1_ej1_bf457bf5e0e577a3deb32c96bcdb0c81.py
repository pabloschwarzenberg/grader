#Nota final
pt = 0
pi = 0
ne = 0
pp = 0
while pt <= 0 and pi <= 0 and ne <= 0 and pp <= 0:
    pt = float(input("Ingrese la nota de las tareas "))
    pi = float(input("Ingrese la nota de las interrogaciones "))
    ne = float(input("Ingrese la nota del examen"))
    pp = float(input("Ingrese la nota de la presentacion"))
pf = (0,3 * pt) + (0,3 * pi) + (0,3 * ne) + (0,1 * pp)
pfr = round (pf, 1)
print (pfr)