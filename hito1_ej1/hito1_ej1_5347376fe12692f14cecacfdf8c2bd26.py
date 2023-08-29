#Nota final

pt = float(input('Ingrese PT: '))
pi = float(input('Ingrese PI: '))
ne = float(input('Ingrese NE: '))
pp = float(input('Ingrese PP: '))

nf = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)

print(round(nf,1))