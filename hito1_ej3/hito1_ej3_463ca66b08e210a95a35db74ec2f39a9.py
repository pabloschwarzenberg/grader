i=int(input('Ingresos: '))
na=int(input('Año nacimiento'))
hi=int(input('Numero hijos'))
pe=int(input('Años pertenencia la banco'))
es=str(input('Estado civil'))
vi=str(input('Urbano o Rural'))
if pe>10 and hi>=2:
    print('APROBADO')
elif es=='C' and hi>3 and 2021-na>=45 and 2021-na<55:
    print('APROBADO')
elif i>2500000 and es=='S' and vi=='U':
    print('APROBADO')
elif i>3500000 and pe>5:
    print('APROBADO')
elif vi=='R' and es=='C' and hi<2:
    print('APROBADO')
else:
    print('REPROBADO')