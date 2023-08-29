#Aprobación de créditos
ingresos= int(input('Ingreso (en pesos): '))
nacimiento= int(input('Año de nacimiento: '))
hijos= int(input('Numero de hijos: '))
pertenecia= int(input('Años de pertenencia al banco: '))
estado= input('Estado civil ("S": soltero, "C", casado): ')
zona= input('¿Vive en campo o cuidad? ("U": urbano, "R": rural): ')

edad= 2020-nacimiento

if pertenecia >= 10 and hijos >= 2:
    print('APROBADO')
elif estado == 'C' and hijos >= 3 and 45 <= edad <= 55:
    print('APROBADO')
elif ingresos >= 2500000 and estado == 'S' and zona == 'U':
    print('APROBADO')
elif ingresos >= 3500000 and pertenecia >= 5:
    print('APROBADO')
elif zona == 'R' and estado == 'C' and hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO') 