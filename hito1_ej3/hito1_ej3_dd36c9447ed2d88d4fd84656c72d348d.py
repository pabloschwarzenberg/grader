#Aprobación de créditos
ingreso=int(input('ingresos: '))
nacimiento=int(input('año de nacimiento: '))
n=int(input('número de hijos: '))
pertenencia=int(input('año de pertenencia: '))
print('S:soltero, C:Casado')
estado=input('estado civil: ')
c=0
s=1
print('U:urbano, R:rural')
ur=input('urbano o rural: ')
u=0
r=1

if pertenencia==10 and n>=2:
    print('APROBADO')
if estado==c and n>3 and nacimiento==1973:
    print('APROBADO')
if ingreso<=2500000 and estado==s and ur==r:
    print('APROBADO')
if ingreso<=3500000 and pertenencia>5:
    print('APROBADO')
if ur==u and estado==c and n<2:
    print('APROBADO')
else:
    print('RECHAZADO')
