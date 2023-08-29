#Aprobación de créditos
ingreso = int(input())
edad = 2017 - int(input())
hijos = int(input())
banco = int(input())
estado_civil = input().lower()
lugar_donde_vive = input().lower()
regla_1 = banco > 10 and hijos >= 2
regla_2 = estado_civil == 'c' and hijos > 3 and 45 < edad < 55
regla_3 = ingreso >= 2500000 and estado_civil == 's' and lugar_donde_vive == 'u'
regla_4 = ingreso >= 3500000 and banco > 5
regla_5 = lugar_donde_vive = 'r' and hijos < 2
if regla_1 or regla_2 or regla_3 or regla_4 or regla_5:
    print('APROBADO')
else:
    print('RECHAZADO')
