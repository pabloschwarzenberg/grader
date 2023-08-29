#Aprobación de créditos
      
ingreso = int(input('Indique sus ingresos (En Pesos): '))
nacimiento = int(input('Indique año de nacimiento: '))
hijos = int(input('Ingrese numero de hijos: '))
antiguedad = int(input('Ingrese años en en banco: '))
civil = input('Indique estado civil [S]Soltero o [C]Casado: ')
direccion = input('Indique donde vive [U]Urbano o [R]Rural: ')

edad = 2021 - nacimiento

if (antiguedad > 10) and (hijos >= 2):
    print('APROBADO')
elif ((civil == 'C') or (civil == 'c')) and (hijos > 3) and ((edad >= 45) and (edad <= 55)):
    print('APROBADO')
elif (ingreso > 2500000) and ((civil == 'S') or (civil == 's')) and ((direccion == 'U') or (direccion == 'u')):
    print('APROBADO')
elif (ingreso > 3500000) and (antiguedad > 5):
    print('APROBADO')
elif ((direccion == 'R') or (direccion == 'r')) and ((civil == 'C') or (civil == 'c')) and (hijos < 2):
    print('APROBADO')
else:
    print('RECHAZADO')