#Aprobación de créditos
i = int(input('Ingrese sus ingresos: '))
a = int(input('Ingrese au año de nacimiento: '))
e = 2021 - a
nh = int(input('¿Cuántos hijos tienes? '))
ap = int(input('¿Cuánto tiempo has sido parte de nuestro banco? '))
es = input('¿Cuál es su estado Civil? "S" para Soltero / "C" para Casado: ')
cc = input('¿Dónde vive usted? "U" para Ciudad / "R" para Campo: ')
if((ap > 10) and (nh >= 2)):
    print('APROBADO')
if((es == 'C') and (nh > 3) and (e == [45,46,47,49,50,51,52,53,54,55])):
    print('APROBADO')
if((i > 2500000) and (es == 'S') and (cc == 'U')):
    print('APROBADO')
if((i > 3500000) and (ap > 5)):
    print('APROBADO')
if((cc == 'R') and (es == 'C') and (nh < 2)):
    print('APROBADO')
else:
    print('RECHAZADO')