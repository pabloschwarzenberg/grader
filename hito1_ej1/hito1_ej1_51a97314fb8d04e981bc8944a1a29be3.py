#Nota final
pt = float(input("Ingrese PT: "))
pi = float(input("Ingrese PI: "))
ne = float(input("Ingrese NE: "))
pp = float(input("Ingrese PP: "))

promedioFinal = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

print("%s" % round(promedioFinal, 1))
