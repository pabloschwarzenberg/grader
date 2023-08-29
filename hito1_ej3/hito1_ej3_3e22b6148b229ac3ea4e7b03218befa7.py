#Aprobación de créditos
x = int(input('Ingrese su ingreso en pesos: '))
y = int(input('Ingrese su año de nacimiento: '))
z = int(input('Ingrese su numero de hijos: '))
a = int(input('Ingrese sus años de pertenencia al banco: '))
b = input('Ingrese su estado civil ("S": soltero, "C", casado): ')
c = input('Ingrese si vive en campo o cuidad ("U": urbano, "R": rural): ')

if (a>10 and 2<=z) or (b=="C" and 3<z and 1965<=y<=1975) or (x>2500000 and b=="S" and c==U) or (x>3500000 and a>5) or (c=="R" and b=="C" and 2>z):
    print('APROBADO')
else:
            print('RECHAZADO')
