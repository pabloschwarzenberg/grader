#Aprobación de créditos
ingreso=int(input('Digite el ingreso en pesos: '))  
anonac=int(input('Año de nacimiento: ')) 
hijos=int(input('Número de hijos: ')) 
anosbanco=int(input('Años de pertenencia al banco: ')) 
ecivil=input('Ingrese "S" si es soltero y "C" si es casado: ')
vivienda=input('Ingrese "U" si vive en sector urbano y "R" si vive en el sector rural: ')
if anosbanco >= 10 and hijos >=2:
    print('APROBADO')
elif ecivil== 'C' and hijos > 3 and  1965 <= anonac <= 1975:
    print('APROBADO')
elif ingreso > 2500000 and ecivil== 'S' and vivienda== 'U':
    print('APROBADO')
elif ingreso > 3500000 and anosbanco >=5:
    print('APROBADO')
elif vivienda == 'R' and ecivil== 'C' and hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')
  