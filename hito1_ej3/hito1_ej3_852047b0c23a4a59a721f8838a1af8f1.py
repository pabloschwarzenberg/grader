ing = int(input('ing: '))
nac = int(input('nac: '))
nhi = int(input('nhi: '))
apb = int(input('apb: '))
esc = input('esc: ')
urv = input('urv: ')

if apb > 10 and nhi >= 2:
    print('APROBADO')
elif esc == 'C' and nhi >= 3 and 45 <= 2023 - nac <= 55:
    print('APROBADO')
elif ing > 2500000 and esc == 'S' and urv == 'U':
    print('APROBADO')
elif ing > 3500000 and apb > 5:
    print('APROBADO')
elif urv == 'R' and esc == 'C' and nhi < 2:
    print('APROBADO')
else:
    print('RECHAZADO')