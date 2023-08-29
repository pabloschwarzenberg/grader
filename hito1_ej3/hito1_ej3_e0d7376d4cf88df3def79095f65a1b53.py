#Aprobación de créditos
ingreso = int(input('Ingreso en pesos: '))
ano_nacimiento = int(input('Ano: '))
numero_hijo = int(input('hijos: '))
pertenencia_banco = int(input('pertenencia al banco: '))
estado_civil = input('estado civil: ')
vive =  input('Ingrese donde vive: ')
if pertenencia_banco >= 10 and  numero_hijo >= 2:
    print('credito aprobado')
elif (2021- ano_nacimiento)>= 45 and(2021- ano_nacimiento)<= 55 and estado_civil == "C" and numero_hijo >= 3:
    print('credito aprobado')
elif ingreso >= 2500000 and estado_civil == 'S' and vive == 'C':
    print('credito aprobado')
elif ingreso >= 3500000 and pertenencia_banco >= 5:
    print('credito aprobado')
elif vive == 'R' and estado_civil == 'C' and numero_hijo < 2:
    print('credito aprobado')
else:
    print('credito no aprobado')