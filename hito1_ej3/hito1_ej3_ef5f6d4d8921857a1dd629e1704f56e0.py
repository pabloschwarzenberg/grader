#Aprobación de créditos
import datetime

income = int(input('Ingreso: '))
birth_year = int(input('Año de nacimiento: '))
children = int(input('Número de hijos: '))
membership_duration = int(input('Años de pertenencia al banco: '))
marital_status = input('Estado civil: ')
location_type = input('Tipo de locación: ')

age = datetime.datetime.now().year - birth_year

if ((membership_duration > 10 and children >=2) or
    (marital_status == 'C' and children > 3 and 45 <= age <= 55) or
    (income > 2500000 and marital_status == 'S' and location_type == 'U') or
    (income > 3500000 and membership_duration > 5) or
    (location_type == 'R' and marital_status == 'C' and children < 2)):
  print('APROBADO')
else:
  print('RECHAZADO')