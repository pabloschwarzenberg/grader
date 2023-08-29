#Nota final
pt = float(input('Ingrese la nota que obtuvo en la tarea: '))
pi = float(input('Ingrese la nota que obtuvo en la interrogación: '))
ne = float(input('Ingrese la nota que obtuvo en el exámen: '))
pp = float(input('Ingrese la nota que obtuvo en la presentación: '))
ppp = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
ppp2 = round(ppp, 1)
print('Su nota final es: ', ppp2)
      