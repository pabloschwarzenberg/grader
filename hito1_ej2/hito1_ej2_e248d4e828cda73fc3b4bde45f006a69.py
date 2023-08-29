phone_number = int(input('Ingrese numero telefonico: '))
call_time = int(input('Ingrese hora de la llamada: '))

if 0 <= call_time < 7:
    print('Resultado: CONTESTAR')
elif 7 <= call_time < 14:
    if str(phone_number).endswith('909'):
        print('Resultado: CONTESTAR')
    else:
        print('Resultado: NO CONTESTAR')
elif 14 <= call_time < 17:
    print('Resultado: NO CONTESTAR')
elif 17 <= call_time < 19:
    if str(phone_number).startswith('877'):
        print('Resultado: NO CONTESTAR')
    else:
        print('Resultado: CONTESTAR')
else:
    print('Resultado: NO CONTESTAR')
    