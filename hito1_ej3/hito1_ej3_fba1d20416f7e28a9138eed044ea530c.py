#Aprobación de créditos
x = 'APROBADO'
y = 'RECHAZADO'

print('Bienvenido, este es el sistema de atención automatizada de créditos de consumo')
print('A continuación se te pedirán ciertos datos: ')
ip = int(input('Favor ingresar sueldo bruto mensual: '))
an = int(input('Ingresar año de nacimiento: '))
#an1 = int(input('Si ya estuvo de cumpleaños este año marque 1, sino, marque 2: '))
#if an1 == 1:
ed = 2020 - an
#elif an1 == 2:
#    ed = 2020 - an - 1
nh = int(input('Ingresar número de hijos/as: '))
ab = int(input('Ingresar años de antiguedad como cliente de nuestro banco: '))
ec = str(input('Ingrese su estado civil: soltero con la letra [S] y casado con la letra [C] :'))
ur = str(input('Ingrese si vive en campo/zona rural con una [R] o ciudad/zona urbana con un [U]: '))

if ab > 10 and nh >= 2:
    print(x)
elif ec == 'C' and nh > 3 and ed >= 45 and ed <= 55:
    print(x)
elif ip > 2500000 and ec == 'S' and ur == 'U':
    print(x)
elif ip > 3500000 and ab > 5:
    print(x)
elif ur == 'R' and ec == 'C' and nh < 2:
    print(x)
else:
    print(y)