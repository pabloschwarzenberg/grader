#datos del cliente 
ingreso=int(input('ingreso mensual en pesos: '))
nacimiento=int(input('cuando nacio: '))
num_hijos=int(input('numero de hijos: '))
pertenencia=int(input('tiempo de pertenencia en el banco: '))
estado_civil=input('ingresar el estado civil (S para soltero,C para casado): ')
ubicacion=input('ingrsar la ubicacion(U para urbano, R para rural): ')

#reglas para aprobar el credito
if pertenencia > 10 and num_hijos >= 2:
    print('aprobado')
elif estado_civil == 'C' and num_hijos > 3 and 45 <= (2023 - nacimiento) <=55:
    print('aprobado')
elif ingreso > 25000000 and estado_civil == 'S' and ubicacion == 'U':
    print('aprobado')
elif ingreso > 35000000 and pertenencia > 5:
    print('aprobado')
elif ubicacion == 'R' and estado_civil == 'C' and num_hijos < 2:
    print('arpobado')
else:
    print('rechazado')
