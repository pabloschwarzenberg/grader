#Zodiaco
dt = int (input ('Ingrese su dia de cumpleaños porfavor: '))
mnth = int (input ('Ingrese su mes de cumpleaños porfavor: '))
if (dt>=21 and mnth==3) or (dt<=20 and mnth==4):
    print ('Su signo zodiacal es: Aries!')
if (dt >= 21 and mnth == 4) or (dt <= 21 and mnth == 5):
    print('Su signo zodiacal es: Tauro!')
if (dt >= 22 and mnth == 5) or (dt <= 21 and mnth == 6):
    print('Su Signo zodiacal es: Geminis!')
if (dt>=21 and mnth==6) or (dt<=23 and mnth==7):
    print ('Su Signo zodiacal es: Cancer!')
if (dt >= 24 and mnth == 7) or (dt <= 23 and mnth == 8):
    print('Su Signo zodiacal es: Leo!')
if (dt >= 24 and mnth == 8) or (dt <= 23 and mnth == 9):
    print('Su Signo zodiacal es: Virgo!')
if (dt>=24 and mnth==9) or (dt<=23 and mnth==10):
    print ('Su Signo zodiacal es: Libra!')
if (dt>=24 and mnth==10) or (dt<=22 and mnth==11):
    print ('Su Signo zodiacal es: Escorpio!')
if (dt>=23 and mnth==11) or (dt<=21 and mnth==12):
    print ('Su Signo zodiacal es: Sagitario!')
if (dt>=22 and mnth==12) or (dt<=20 and mnth==1):
    print ('Su Signo zodiacal es: Capricornio!')
if (dt>=21 and mnth==1) or (dt<=19 and mnth==2):
    print ('Su Signo zodiacal es: Acuario!')
if (dt>=20 and mnth==2) or (dt<=20 and mnth==3):
    print ('Su Signo zodiacal es: Piscis!')