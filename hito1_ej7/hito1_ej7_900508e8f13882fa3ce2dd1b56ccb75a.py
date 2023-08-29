dia = int(input('Ingrese el día de su nacimiento: '))
mes = int(input('Ingrese su mes de nacimiento en números: '))

if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=19)): ##Aries
    print('Signo: Aries.')

if ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=20)):  ##Tauro
    print('Signo: Tauro.')

if ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=21)):  ##Géminis
    print('Signo: Geminis.')

if ((mes==6) and (dia>=22)) or ((mes==7) and (dia<=22)):  ##Cáncer
    print('Signo: Cancer.')

if ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=23)):  ##Leo
    print('Signo: Leo.')

if ((mes==8) and (dia>=24)) or ((mes==9) and (dia<=22)):  ##Virgo
    print('Signo: Virgo.')

if ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=23)):  ##Libra
    print('Signo: Libra.')

if ((mes==10) and (dia>=24)) or ((mes==11) and (dia<=22)):  ##Escorpio
    print('Signo: Escorpio.')

if ((mes==11) and (dia>=23)) or ((mes==12) and (dia<=22)):  ##Sagitario
    print('Signo: Sagitario.')

if ((mes==12) and (dia>=23)) or ((mes==1) and (dia<=20)):  ##Capricornio 
    print('Signo: Capricornio.')

if ((mes==1) and (dia>=21)) or ((mes==2) and (dia<=18)):  ##Acuario
    print('Signo: Acuario.')

if ((mes==2) and (dia>=19)) or ((mes==3) and (dia<=20)):  ##Piscis
    print('Signo: Piscis.')
