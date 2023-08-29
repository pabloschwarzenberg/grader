#Aprobación de créditos
#Aprobación de créditos
i=int(input('ingrese su ingreso:'))
a=int(input('ingrese su año de nacimiento:'))
h=int(input('ingrese su numero de hijos:'))
antiguedad=int(input('ingrese su antiguedad en el banco:'))
c=input('ingrese su estado civil, soltero=S, casado=D')
lugar=input('ingrese si vive en campo=R, ciudad=U')
edad=2020-a
if antiguedad>=10 and h>=2:
  print('APROBADO')
if c=='D' and h>3 and 45<=edad<=55:
  print('APROBADO')
if i>2500000 and c==S and lugar=='U':
  print('APROBADO')
if i>3500000 and antiguedad>5:
  print('APROBADO')
if lugar=='R'and c=='C' and h<2:
  print('APROBADO')
else:
  print('RECHAZADO')