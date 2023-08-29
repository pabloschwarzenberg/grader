ingreso = eval(input('ingreso:'))
nacimiento = eval(input('anio nacimiento:'))
hijos = eval(input('numero de hijos:'))
banco =eval(input('anios en el banco:'))
estado_civil = str(input('soltero o casado:'))
vivienda = str(input('ciudad o campo:'))
S=str('soltero')
C=str('casado')
U=str('ciudad')
R=str('campo')
 

 
if banco > 10 and hijos >= 2:
 print('APROBADO')
elif estado_civil =='C' and hijos > 3 and nacimiento >= 1975 and nacimiento <= 1965:
 print('APROBADO')
elif ingreso > 2500000 and (str(estado_civil == 'S' and vivienda == 'U')):
 print('APROBADO')
if ingreso > 3500000 and banco > 5:
 print('APROBADO')
if vivienda == 'R' and estado_civil == 'C' and hijos == 1:
 print('APROBADO')
else:
 print('RECHAZADO')