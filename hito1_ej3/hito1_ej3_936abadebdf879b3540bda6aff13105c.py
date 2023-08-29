#Aprobación de créditos
ing = int(input('Ingreso total en pesos: '))
a = int(input('Año de nacimmiento: '))
nh = int(input('Numero de hijos: '))
pb = int(input('Años de pertenencia al banco: '))
ec = str(input('Estado civil (S: soltero, C: casado): '))
dmc = str(input('Zona de domicilio (U: urbano, R: rural): '))
if pb > 10 and nh >= 2 or ec == 'C' and nh > 3 and 1965 < a <1975 or ing > 2500000 and ec == 'S' and dmc == 'U' or ing > 3500000 and pb > 5 or dmc == 'R' and ec == 'C' and nh < 2:
    print('APROBADO')
else:
    print('RECHAZADO')      