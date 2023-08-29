#Contestador de celular

llamada = int(input("Ingrese numero telefonico: "))
horaLlamada = int(input("Ingrese hora de la llamada: "))
llamadaStr = str(llamada)
llamada1 = llamadaStr[5]
llamada2 = llamadaStr[6]
llamada3 = llamadaStr[7]

llamada4 = llamadaStr[0]
llamada5 = llamadaStr[1]
llamada6 = llamadaStr[2]

llamadaSum2 = llamada4+llamada5+llamada6
llamadaSum = llamada1+llamada2+llamada3

if horaLlamada > 0 and horaLlamada < 7:
    print('CONTESTAR')
if horaLlamada > 19:
    print('NO CONTESTAR')

if horaLlamada < 14:
    if llamadaSum == '909':
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')

if horaLlamada >= 17 and horaLlamada <= 19:
    if llamadaSum2 == '877':
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')