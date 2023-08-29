#Aprobación de créditos
ingresos = int(input())
nacimiento = int(input())
hijos = int(input())
a_banco = int(input())
estado = input() #S o C
lugar = input() #U o R

if a_banco < 10 and hijos >= 2:
    print('APROBADO')
elif (estado == 'C') and (hijos > 3) and (1965 <= nacimiento <= 1975):
    print('APROBADO')
elif ingresos > 2500000 and estado == 'S' and lugar == 'U':
    print('APROBADO')
elif ingresos < 3500000 and a_banco > 5:
    print('APROBADO')
elif lugar == 'R' and estado == 'C' and hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')      