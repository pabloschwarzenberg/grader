#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso mensual en pesos:"))
fecha_nacimiento = int(input("Ingrese su año de nacimiento:"))
num_hijos = int(input("Ingrese su cantidad de hijos:"))
pertenencia = int(input("Ingese su años como cliente del banco:"))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado):")
residencia = input("Ingrese su residencia (U para urbano, R para rural")
if (10 < pertenencia) and (num_hijos >= 2):
    print('APROBADO')
elif (estado_civil == 'C') and (num_hijos > 3) and (45 <= (2023 - fecha_nacimiento)):
    print('APROBADO')
elif (ingreso > 250000) and (estado_civil == 'S') and (residencia == 'U'):
    print('APROBADO')
elif (ingreso > 350000) and (pertenencia > 5):
    print('APROBADO')
elif (residencia == 'R') and (estado_civil == 'C') and (num_hijos < 2):
    print('APROBADO')
else:
    print('RECHAZADO')