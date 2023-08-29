ingreso = int(input('ingreso (en pesos): '))

nacimiento = int(input('Año de nacimiento: '))

hijos = int(input('Numero de hijos: '))

pertenencia = int(input('Años de pertenencia al banco: '))

civil = str(input('Estdo civil ("S": Soltero, "C", casado: '))

vive = str(input('Si vive en campo o ciudad ("U": urbano, "R": rural: '))

a = 'APROBADO'
b = 'RECHAZADO'

edad = 2021-nacimiento


if(pertenencia>=10 and hijos>=2):
    print(a)

elif(civil=='C' and hijos>=3 and edad>44 and edad<=55):
    print(a)

elif(ingreso>=2500000 and civil=='S' and vive=='U'):
    print(a)

elif(ingreso>=3500000 and pertenencia>=5):
    print(a)

elif(vive=='R' and civil=='C' and hijos<2):
    print(a)

else:
    print(b)