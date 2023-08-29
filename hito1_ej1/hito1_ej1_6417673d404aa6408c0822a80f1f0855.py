pt, pi, ne, pp = 0, 0, 0, 0

while 7 < pt or pt < 1: # 7 > pt > 1
    pt = float(input("Ingrese su promedio de notas:\n>"))
pt = round(pt, 1)

while 7 < pi or pi < 1: # 7 > pi > 1
    pi = float(input("Ingrese su promedio de interrogaciones:\n>"))
pi = round(pi, 1)

while 7 < ne or ne < 1: # 7 > ne > 1
    ne = float(input("Ingrese la nota de examen:\n>"))
ne = round(ne, 1)

while 7 < pp or pp < 1: # 7 > pp > 1
    pp = float(input("Ingrese su promedio de presentación:\n>"))
pp = round(pp, 1)

print(round((pt * 0.3) + (pi * 0.3) + (ne * 0.3) + (pp * 0.1), 1))