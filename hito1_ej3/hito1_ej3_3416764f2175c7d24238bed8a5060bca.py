i=eval(input('ingrese ingresos:'))
an=eval(input('ingrese año de nacimiento:'))
nh=eval(input('ingrese numero de hijos:'))
ap=eval(input('ingrese años de pertenencia al banco:'))
ec=str(input('ingrese estado civil:'))
cc=str(input('ingrese campo o ciudad:'))
edad=2020-an
casado='C'
soltero='S'
urbano='U'
rural='R'
if (ap>10 and nh>=2) or (ec=='C' and nh>3 and 45<edad<55) \
or (i>2500000 and ec=='S' and cc=='U') or (i>3500000 and ap>5) \
or (cc=='R' and ec=='C' and nh<2):
    print('APROBADO')
else:
    print('RECHAZADO')