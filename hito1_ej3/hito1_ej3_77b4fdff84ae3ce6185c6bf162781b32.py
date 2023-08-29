#Aprobación de créditos
i= eval(input('ingrese los ingresos:'))
an= eval(input('ingrese años de nacimiento:'))
n= eval(input('ingrese numero de hijos:'))
a= eval(input('ingrese años de pertenencia al banco:'))
sc= str(input('ingrese estado civil:'))
cc= str(input('ingrese campo o ciudad:'))

edad=2020-an

soltero='S'
casado='C'
ciudad='U'
campo='R'

if (a>10 and n>=2) or (sc=='C' and n>3 and 45<edad<55) or (i>2500000 and sc=='S' and cc== 'U')\
   or (i>3000000 and a>5) or (cc=='R' and sc=='C' and n<2):
    print('APROBADO')
else:
    print('RECHAZADO')  
