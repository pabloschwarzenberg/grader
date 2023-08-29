#Descomponer un número
numero = str(input('ingresar numero hasta 4 digitos'))
if len(numero) == 4:
  mil = str(numero[0]) + 'M'
  cen = str(numero[1]) + 'C'
  dec = str(numero[2]) + 'D'
  un = str(numero[3]) + 'U'
  print(mil, cen, dec, un, sep='+')
elif len(numero) == 3:
  cen = str(numero[0]) + 'C'
  dec = str(numero[1]) + 'D'
  un = str(numero[2]) + 'U'
  print(cen, dec, un, sep='+')
elif len(numero) == 2:
  dec = str(numero[0]) + 'D'
  un = str(numero[1]) + 'U'
  print(dec, un, sep='+')
elif len(numero) == 1: 
  un = str(numero[0]) + 'U'
  print(un)