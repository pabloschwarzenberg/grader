print( 'Ingrese sus datos a continuacion' )

i= int(input('Ingresos en pesos: '))
n= int(input('Ingrese su año de nacimiento: '))
h= int(input('Ingrese el numero de hijos: '))
p= int(input('Ingrese los años que ha pertenecido al banco: '))
e= input('Ingrese si es soltero con la letra (S) o si es casado con la letra (C): ')
c= input('Ingrese si vive en campo con la letra (R) o si vive en ciudad con la letra (U): ')
E= 2020-n
e = 'S'
e = 'C'
c = 'R'
c = 'U'
w = 10<p and 2<=h
x = e=='C' and 3<h and 45<=E<=55
y = 2500000<i and e=='S' and c=='U'
z = 3500000<i and p<5
f = c=='R' or e=='C' and 0<=h<2

if e!='S' and e!='C':
    print('No digitaste tu estado civil correcto')
elif c!='R' and c!='U':
    print('No digitaste tu zona de vivienda')
elif 0>h or 1921>n or 0>=p:
    print('Unas de las cifras ingresadas no es correcta')
elif 10<p and 2<=h:
    print('APROBADO')
elif e=='C' and 3<h and 45<=E<=55:
    print('APROBADO')
elif 2500000<i and e=='S' and c=='U':
    print('APROBADO')
elif 3500000<i and p<5:
    print('APROBADO')
elif e=='C'or c=='R' and 0<=h<2:
    print('APROBADO')
elif not w and not x and y and z and not f:
    print('RECHAZADO')

