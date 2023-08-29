#Aprobación de créditos
ingresos = int(input('Ingrese sus ingresos(pesos): '))
nacimiento = int(input('Ingrese su año de nacimiento: '))
hijos = int(input('Ingrese su numero de hijos: '))
año_pertenencia_banco = int(input('Ingrese los años de pertenencia al banco: '))
estado_civil = input('Ingrese si su estado civil es soltero(S) o Casado(C): ')
vivienda = input('Ingrese si vive en campo(R) o ciudad(U): ')

if año_pertenencia_banco > 10 and hijos >= 2:
    print('El credito esta APROBADO')
elif estado_civil == 'C' and hijos > 3 and nacimiento >= 1977 and nacimiento <= 1967 :
    print('El credito esta APROBADO')
elif ingresos > 2500000 and estado_civil == 'S' and vivienda == 'U':
    print('El credito esta APROBADO')
elif ingresos > 3500000 and año_pertenencia_banco > 5:
    print('El credito esta APROBADO')
elif vivienda == 'R' and estado_civil == 'C' and hijos < 2:
    print('El credito esta APROBADO')
else:
    print('El credito esta REPROBADO')      