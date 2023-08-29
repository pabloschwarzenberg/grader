print('Llene con sus datos')
i = int(input('Ingresos                    : '))
a = int(input('Año de nacimiento           : '))
h = int(input('Número de hijos             : '))
pb = int(input('Años de pertenencia al banco: '))
ec = input('Estado civil                : ')      
v = input('Dónde vive                  : ')
edad = 2022 - a
if pb >= 10 and h >= 2 or ec == 'C' or 'c' and h > 3 and 45<=a>=55 or i >= 250000 and ec == 'S' or 's' and v == 'U' or i >= 3500000 and pb > 5 or v == 'R' and ec == 'C' or 'c' and h < 2:
 print('APROBADO')
