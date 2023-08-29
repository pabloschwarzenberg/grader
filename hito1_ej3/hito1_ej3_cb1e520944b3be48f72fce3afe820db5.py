#APROBACIONDECREDITOS
v1= int(input('¿A cuanto asciende su sueldo?: '))
v2= int(input('¿En que año nacio?: '))
v3= int(input('¿Cuantos hijos nacidos hasta la fecha?: '))
v4= int(input('¿Hace cuantos años trabaja en el Banco?: '))
print('Las siguientes letras identifican su estado civil.\n S: soltero \t C: casado')
v5=input('Escriba la letra asociada: ')
print('Las siguientes letras identifican su residencia.\n U: urbano \t R: rural')
v6=input('Escriba la letra correspondiente: ')
v7=2016-v2
#proceso
if v1>10 and v4>=2:
      print('APROBADO')
elif v5=='C' and v4<3 and 45<v7<55:
      print('APROBADO')
elif v1>2500000 and v5=='S' and v6=='U':
      print('APROBADO')
elif  v1>3500000 and v4>5:
      print('APROBADO')
elif v6=='U' and v5=='C' and v3<2:
      print('APROBADO')
else:
      print('RECHAZADO')
