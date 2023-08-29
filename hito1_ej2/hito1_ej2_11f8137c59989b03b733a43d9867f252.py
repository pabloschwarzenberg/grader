#Contestador de celular
Número=int(input('Ingrese su número: '))
Hora=int(input('¿Qué hora es?(Sólo la hora, sin los minutos): '))
if (0>=Hora<=7) or (Hora<14 and Número%1000==909) or (17>=Hora<=19 and int(Número/10000)!=877):
    print('CONTESTAR')
elif Hora>19:
    print('NO CONTESTAR')
else:
    print('NO CONTESTAR')
     