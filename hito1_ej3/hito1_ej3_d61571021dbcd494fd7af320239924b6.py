#Aprobación de créditos
Ingreso = int(input('Ingreso (en pesos): '))
bird_day = int(input('Años de pertenencia al banco: '))
Child_num = int(input('Año de nacimiento: '))
bank_yr = int(input('Número de hijos: '))
Stt_civil = str(input('Estado civil ("S": soltero, "C", casado): '))
Zone = str(input('Si vive en campo o cuidad ("U": urbano, "R": rural): '))

if bank_yr > 10 and Child_num >= 2:
        print('APROBADO')

elif Stt_civil == 'C' and Child_num > 3 and 45 < (2020-bird_day) < 55:
        print('APROBADO')

elif Ingreso < 2500000 and Stt_civil == 'S' and Zone == 'U':
        print('APROBADO')

elif Ingreso < 3500000 and bank_yr > 5:
        print('APROBADO')

elif Zone == 'R' and Stt_civil == 'C' and Child_num < 2:
    print('APROBADO')  

else:
    print('RECHAZADO')