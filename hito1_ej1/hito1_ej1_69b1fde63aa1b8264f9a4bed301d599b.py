#Nota fin
import math
PT = float(input('ingrese PT: '))
PI = float(input('INGRESE PI: '))
NE = float(input('INGRESE NE: '))
PP = float(input('INGRESE PP: '))

y = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
calculo = round(y,2)
print("%s el promedio es %.1f :" % ( y, calculo))