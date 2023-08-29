#Aprobación de créditos
S=-1
C=-2
U=-3
R=-4
i=eval(input('Ingreso:'))
a=eval(input('Año de nacimiento:'))
h=eval(input('Número de hijos:'))
t=eval(input('Años de pertenencia al banco:'))
e=eval(input('Estado civil ("S": soltero, "C", casado):'))
v=eval(input('Si vive en campo o cuidad ("U": urbano, "R": rural):'))
an=2020-a
if t>10 and h>=2:
    print('APROBADO')
if e==-2 and h>3 and 45<=an<=55:
    print('APROBADO')
if i>2500000 and e==-1 and v==-3:
    print('APROBADO')
if i>3500000 and t>5:
    print('APROBADO')
if v==-4 and e==-2 and h<2:
    print('APROBADO')
else:
    print('RECHAZADO')      