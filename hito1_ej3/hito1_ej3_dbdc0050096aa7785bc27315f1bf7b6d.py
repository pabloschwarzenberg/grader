#Aprobación de créditos
ingresos = eval(input('Ingresos (en pesos): '))
ano_nacimiento = int(input('Año de nacimiento: '))
num_hijos = int(input('Numero de hijos: '))
anos_enbanco = int(input('Años de pertenencia al banco: '))
estado_civil = input('Estado civil ("S":soltero, "C":casado): ')
vivienda = input('Vive en ("U":urbano, "R":rural): ')

if anos_enbanco > 10 and num_hijos >= 2:
    print('APROBADO')

elif estado_civil == 'C' and num_hijos > 3 and ano_nacimiento >= 1978 and ano_nacimiento <= 1968:
    print('APROBADO')

elif ingresos > 3500000 and anos_enbanco > 5:
    print('APROBADO')

elif vivienda == 'R' and num_hijos < 2:
    print('APROBADO')

else:
    print('RECHAZADO')     