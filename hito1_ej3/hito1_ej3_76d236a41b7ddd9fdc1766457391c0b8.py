#Aprobación de créditos
i=int(input('Su ingreso en pesos: '))
an=int(input('Año de nacimiento: '))
e=2020-an
h=int(input('Numero de hijos: '))
ab=int(input('Años en el banco: '))
ec=input('S: soltero, C: casado: ')
cc=input('U: urbano, R: rural: ')

if ab>10 and h>=2:
    print('APROBADO')
elif ec=="C" and h>3 and 45<=e<=55:
    print('APROBADO')
elif i>2500000 and ec=="S" and cc=="U":
    print('APROBADO')
elif i>3500000 and ab>5:
    print('APROBADO')
elif cc=="R" and ec=="C" and h<2:
    print('APROBADO')
else:
    print('RECHAZADO')      