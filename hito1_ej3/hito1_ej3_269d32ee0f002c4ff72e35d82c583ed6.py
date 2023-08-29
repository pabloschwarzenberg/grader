#Aprobación de créditos
ingresos = int(input('Ingrese sus ingresos, por favor: '))
edad = int(input('Ingrese su edad, por favor: '))
hijos = int(input('Ingrese su cantidad de hijos, por favor: '))
pertenencia  = int(input('Ingrese su pertenencia al banco, por favor: '))
estado = input('Ingrese su Estado Civil: ')
cor = input('Ingrese si vive en zona Urban o Rural: ')

if (pertenencia>10 and hijos>=2) or (estado=='C' and hijos>3 and 45<edad<55):
    print('APROBADO')

elif (ingresos>2500000 and estado=='S' and cor=='U') or (ingresos>3500000 and pertenencia > 5):
    print('APROBADO')

elif cor=='R' and estado=='C' and hijos<2:
    print('APROBADO')

else:
    print('RECHAZADO')
      