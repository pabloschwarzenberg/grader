#Aprobación de créditos
Ingreso = int(input('ingrese un monto en pesos: ' ))
nacimiento = int(input('ingrese año de nacimiento: '))
Numero_de_hijos = int(input('ingrese el numero de hijos: '))
banco = int(input('ingre años de pertenencia al banco: '))
Estado_civil = input('ingrese estado civil'',''S: soltero'',' 'C: casado: ')
campo_cuidad = input('ingrese zona en la que vive'',' 'U: urbano'',' 'R: rural: ')
Estado_civil = Estado_civil.upper()
campo_cuidad = campo_cuidad.upper()

if 10<banco and 2<=Numero_de_hijos:
    print('APROBADO')

elif Estado_civil == 'C' and 3<Numero_de_hijos and 1965<=nacimiento<=1975:
    print('APROBADO')

elif 2500000<Ingreso and Estado_civil == 'S' and campo_cuidad == 'U':
    print('APROBADO')

elif 3500000<Ingreso and 5<banco:
    print('APROBADO')

elif campo_cuidad == 'R' and Estado_civil == 'C' and Numero_de_hijos<2:
    print('APROBADO')

else:
    print('RECHAZADO')
     