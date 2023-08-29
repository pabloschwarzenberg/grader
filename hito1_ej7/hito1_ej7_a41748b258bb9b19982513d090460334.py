#Zodiaco
print('El sigiente programa le indicará a qué signo pertenece')
dia = int(input('Ingrese su día de nacimiento: '))
mes = int(input('Ingrese su mes de nacimiento numéricamente: '))
if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=20)):
    print('Su signo corresponde a Aries')
if ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=21)):
    print('Su signo corresponde a Taurus')
if ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=21)):
    print('Su signo corresponde a Geminis')
if ((mes==6) and (dia>=21)) or ((mes==7) and (dia<=23)):
    print('Su signo corresponde a Cancer')
if ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=23)):
    print('Su signo corresponde a Leo')
if ((mes==8) and (dia>=23)) or ((mes==9) and (dia<=23)):
    print('Su signo corresponde a Virgo')
if ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=23)):
    print('Su signo corresponde a Libra')
if ((mes==10) and (dia>=23)) or ((mes==11) and (dia<=22)):
    print('Su signo corresponde a Scorpio')
if ((mes==11) and (dia>=22)) or ((mes==12) and (dia<=22)):
    print('Su signo corresponde a Sagittarius')
if ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=20)):
    print('Su signo corresponde a Capricornio')
if ((mes==1) and (dia>=20)) or ((mes==2) and (dia<=19)):
    print('Su signo corresponde a Aquarius')
if ((mes==2) and (dia>=19)) or ((mes==3) and (dia<21)):
    print('Su signo corresponde a Pisces')