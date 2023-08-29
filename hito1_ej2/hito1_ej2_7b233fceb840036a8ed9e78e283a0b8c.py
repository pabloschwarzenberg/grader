#Contestador de celular

numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))
llamada1 = numero_telefonico%1000
llamada2 = numero_telefonico//100000
#ordenar llamadas en "contestar", " no contestar"

if 0 <= hora_llamada <= 7:
    print('CONTESTAR')
if 7 <= hora_llamada < 14:
    if llamada1 == 909:
        print('CONTESTAR')
    else:
        print('CONTESTAR')
if 17 <= hora_llamada <= 19:
    if llamada1 == 877:
        print('NO CONTESTAR')
    else:
        print(' NO CONTESTAR')
if 19 <= hora_llamada <= 23:
    print ('NO CONTESTAR')      