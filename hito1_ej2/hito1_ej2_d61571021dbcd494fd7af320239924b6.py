#Contestador de celular
num = str(input('Ingrese numero telefonico: '))
call_h = int(input('Ingrese hora de la llamada: '))
print(num[:3])
if call_h < 7 and call_h > 0:
    print(' Resultado: CONTESTAR ')

elif call_h < 14 or num[-3] == 909:
    print(' Resultado: CONTESTAR ')
else:
    pass

if num[:3] == '877':
    print(' Resultado: NO CONTESTAR ')
elif call_h > 17 and call_h < 19:
    print('Resultado: CONTESTAR ')
else:
    pass

if call_h > 19:
    print('Resultado: NO CONTESTAR ')
else:
    pass  