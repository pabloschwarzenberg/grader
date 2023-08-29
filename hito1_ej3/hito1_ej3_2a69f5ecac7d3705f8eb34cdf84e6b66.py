#Aprobación de créditos
ing=eval(input('ingreso:'))
an=eval(input('anio nacimiento:'))
nh=eval(input('numero de hijos:'))
ab=eval(input('anios en el banco:'))
ec=str(input('soltero o casado:'))
cc=str(input('ciudad o campo:'))
S=str('soltero')
C=str('casado')
U=str('ciudad')
R=str('campo')
 

 
if ab>10 and nh>=2:
 print('APROBADO')
elif ec=='C' and nh>3 and an>=1975 and an<=1965:
 print('APROBADO')
elif ing>2500000 and (str(ec=='S' and cc=='U')):
 print('APROBADO')
if ing>3500000 and ab>5:
 print('APROBADO')
if cc=='R' and ec=='C' and nh==1:
 print('APROBADO')
else:
 print('RECHAZADO')   