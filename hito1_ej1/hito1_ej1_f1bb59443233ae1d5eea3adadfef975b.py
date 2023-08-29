PT= float(input('Ingrese PT: '))
PI = float(input('Ingrese PI: '))
NE = float(input('Ingrese NE: '))
PP= float(input('Ingrese PP: '))

Pro = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

Prof= round((Pro), 1)
print('promedio final : %.1f' %(Prof))
