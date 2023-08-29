#Aprobación de créditos

i = eval(input('ingreso:'))
an = eval(input('año de nacimiento:'))
nh = eval(input('numero de hijos:'))
ab = eval(input('años de pertenencia al banco:'))
ec = str(input('estado civil (soltero:"S" o casado:"C")'))
cc = str(input('ciudad o campo (urbano: "U" o rural: "R":'))
S = str('soltero')
C = str('casado')
U = str('ciudad')
R = str('campo')

if ab>10 and nh>=2:
 print('APROBADO')
elif ec=='C' and nh>3 and an>=1975 and an<=1965:
 print('APROBADO')
elif i>2500000 and (str(ec == 'S' and cc == 'U')):
 print('APROBADO')
if i>3500000 and ab>5:
 print('APROBADO')
if cc=='R' and ec=='C' and nh==1:
 print('APROBADO')
else:
 print('RECHAZADO')