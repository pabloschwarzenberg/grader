#Contestador de celular
numero = int(input('Ingrese numero de telefonico:'))
hr = eval(input('Ingrese hora:'))

if 0 <= hr < 7:
    print('Resultado:CONTESTAR')
elif 7 <= hr < 14 and numero%1000==909:
    print('Resultado:CONTESTAR')
elif 7 <= hr < 14:
    print('Resultado:NO CONTESTAR')
elif 14 <= hr < 17:
    print('Resultado:NO CONTESTAR')
elif 17 <= hr < 19 and numero//100000:
    print('Resultado:NO CONTESTAR')
elif 17 <= hr < 19:
    print('Resultado:CONTESTAR')
elif 19 <= hr <=23:
    print('Resultado:NO CONTESTAR')