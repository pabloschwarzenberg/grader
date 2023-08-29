#Aprobación de créditos
i=eval(input('Ingreso: $'))
an=eval(input('Año de naciento: '))
nh=eval(input('N° de hijos: '))
ab=eval(input('Años de pertenencia al banco: '))
ec=input('Soltero(S) ó Casado(C): ')
dv=input('¿Vive en campo(R) o ciudad(U)?: ')

if ab>=10 and nh>=2 or ec=='C' and nh>=3 and 45<=(2020-an)<=55 \
or i==2500000 and ec=='S' and dv=='U' or i==3500000 and ab>=5\
or dv=='R' and nh<=2:
    print('APROBADO')
else:
    print('NEGADO')
