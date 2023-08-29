#Nota final
pt = float(input('Ingrese PT: '))
pi = float(input('Ingrese PI: '))
ne = float(input('Ingrese NE: '))
pp = float(input('Ingrese PP: '))
pm = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
pf = round((pm), 2)
print('Promedio Final es: %.1f' %(pf))