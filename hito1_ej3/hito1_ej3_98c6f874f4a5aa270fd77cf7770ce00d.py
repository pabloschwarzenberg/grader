i = eval(input('Ingreso (en pesos):'))
a = eval(input('Año de nacimiento:'))
n = eval(input('Número de hijos:'))
ap = eval(input('Años de pertenencia al banco:'))
e = input('Estado civil (S: soltero y C: casado):')
v = input('vive en campo o cuidad (U: urbano,R: rural):')


if (ap > 10) and (n >=2):
    print('APROBADO')
elif (e == 'C')and(n>3) and (a >=1985) and (a<=1975): 
        print('APROBADO')
elif (i > 2500000) and (e == 'S') and (v == 'U'):
    print('APROBADO')
elif (i >3500000) and (ap > 5):
    print('APROBADO')
elif (v == 'R') and (e == 'C') and (n < 2):
    print('APROBADO')
else:
    print('RECHAZADO')
