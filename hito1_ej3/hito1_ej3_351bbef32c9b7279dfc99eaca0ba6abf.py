#Aprobación de créditos
x=S = 111
C = 222
U = 333
R = 444

x = eval(input('Ingresos: '))
y = eval(input('Ingrese año de nacimiento: '))
h = eval(input('Numero de hijos: '))
z = eval(input('Año de pertenencia al banco: '))
s = eval(input('Estado civil("S": soltero, "C", casado): '))
u = eval(input('Vive en un lugar("U": urbano, "R": rural): '))

if z > 10 and h >= 2:
    print('APROBADO')
else:
    if s==111 and h>3 and 1965 <= y <= 1975:
        print('APROBADO')
    else:
        if x > 2500000 and s==111 and u==333:
            print('APROBADO')
        else:
            if x > 3500000 and z > 5:
                print('APROBADO')
            else:
                if u==444 and s==222 and h < 2:
                    print('APROBADO')
                else:
                    print('RECHAZADO')
