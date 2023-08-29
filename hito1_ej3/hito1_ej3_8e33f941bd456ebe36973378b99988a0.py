#5 credito

    
i = float(input('ingreso mensual en pesos:'))
a = int(input('Ingrese el ano de nacimiento:'))
h = int(input('ngrese el numero de hijos:'))
p = int(input('Ingrese los anos de pertenencia al banco:'))
e = input('Ingrese el estado civil (S para soltero, C para casado):')
r = input('Ingrese el lugar de residencia (U para urbano, R para rural):')

aprobado = False

if p> 10 and h >= 2:
    aprobado = True
elif e== 'C' and h > 3 and 45 <= (2023 - a) <= 55:
    aprobado = True
elif i > 2500000 and e == 'S' and r == 'U':
    aprobado = True
elif i > 3500000 and p> 5:
    aprobado = True
elif r == 'R' and e == 'C' and h < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")