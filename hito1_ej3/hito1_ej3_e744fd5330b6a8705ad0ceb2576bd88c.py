#Aprobación de créditos
x=int(input('Ingreso: '))
y=int(input('Año de nacimiento:'))
x=int(input('Número de hijos:'))
f=int(input('Años de permanencia en el banco:'))
g=str(input('Estado civil:'))
h=str(input('vivienda:'))
t=(2020-y)
if (f<=10 and x<=2) or str((g=='S') and (x<3)and (45<=t<=55)) or str((x<=2500000)and (g=='S')and str(h=='U')) or ((x<=3500000)and(f<=5)) or str((h=='R')and (g=='C')and(x<2)):
    print('APROBADO')
else:
    print('RECHAZADO')
     