#Aprobación de créditos
ingreso= int(input('Ingreso: '))
anon= int(input('Año de Nacimiento: '))
numero= int(input('Número de Hijos: '))
anop= int(input('Años de Pertenencia al Banco: '))
estado= input('Estado Civil, "S": Soltero, "C": Casado: ')
campociudad= input('Vive en campo o cuidad ("U": urbano, "R": rural): ')

if ((anop>10) and (numero>=2))or (((estado=='C')and (numero>3))and (1961<anon<1971))or ((ingreso>3500000)and (anop>5))or (((campociudad=='R')and(estado=='C'))and(numero<2)):
    print('APROBADO')

else:
        print('RECHAZADO')