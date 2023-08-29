#Zodiaco
 
día = int(input('Insertar día de naciemiento en números: '))
mes = int(input('Insertar mes de nacimiento en números: '))


if ((mes == 3) and (día >= 21)) or ((mes == 4) and (día <= 19)): ##Aries
    print('signo: Aries.')
if ((mes == 4) and (día >= 20)) or ((mes == 5) and (día <= 20)): ##Tauro
    print('signo: Tauro')
if ((mes == 5) and (día >= 21)) or ((mes == 6) and (día <= 20)): ##Géminis
    print('signo: Géminis.')
if ((mes == 6) and (día >= 21)) or ((mes == 7) and (día <= 22)):  ##Cáncer
    print('signo: Cáncer.')
if ((mes == 7) and (día >= 23)) or ((mes == 8) and (día <= 22)): ##Leo
    print('signo: Leo.')
if ((mes == 8) and (día >= 23)) or ((mes == 9) and (día <= 22)): ##Virgo
    print('signo: Virgo.')
if ((mes == 9) and (día >= 23)) or ((mes == 10) and (día <= 22)): ##Libra
    print('signo: Libra.')
if ((mes == 10) and (día >= 23)) or ((mes == 11) and (día <= 21)): ##Escorpio
    print('signo: Escorpio.')
if ((mes == 1) and (día >= 22)) or ((mes == 12) and (día <= 21)): ##Sagitario
    print('signo: Sagitario.')
if ((mes == 2) and (día >= 22)) or ((mes == 1) and (día <= 19)): ##Capricornio
    print('signo: Capricornio.')
if ((mes == 3) and (día >= 20)) or ((mes == 2) and (día <= 18)): ##Acuario
    print('signo: Acuario.')
if ((mes == 4) and (día >= 19)) or ((mes == 3) and (día <= 20)): ##piscis
    print('signo: Piscis.')
    