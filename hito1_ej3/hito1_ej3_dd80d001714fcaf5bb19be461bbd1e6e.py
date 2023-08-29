#Aprobación de créditos
ingreso = int(input('ingreso: '))
nacimiento = int(input('año de nacimiento: '))
edad = 2021-nacimiento
hijos = int(input('Número de hijos: '))
tiempo = int(input('Años de pertenencia al banco: '))
Ecivl = input('Estado civil ("S": soltero, "C", casado): ')
ubicacion = input('campo o cuidad ("U": urbano, "R": rural): ')
A = 'APROBADO'
R = 'RECHAZADO'

if tiempo > 10 and hijos >= 2:
    print(A)

elif Ecivl == 'C' and hijos > 3 and edad >= 45 and edad <=55:
    print(A)

elif ingreso > 2500000 and Ecivl == 'S' and ubicacion == 'U':
    print(A)

elif ingreso > 3500000 and tiempo > 5:
    print(A)

elif ubicacion == 'R' and Ecivl == 'C' and hijos < 2:
    print(A)

else:
    print(R)