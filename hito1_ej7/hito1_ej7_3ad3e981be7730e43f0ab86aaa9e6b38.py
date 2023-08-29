dia = int(input('ingresa tu dia de nacimiento: '))
mes = int(input('ingresa tu mes de nacimiento: '))

if mes==3 and dia>21 and dia<=31 or mes==4 and dia>=1 and dia <=20:
    print('ARIES')
if mes==4 and dia>20 and dia<=30 or mes==5 and dia>=1 and dia <=21:
    print('TAURO')
if mes==5 and dia>21 and dia<=31 or mes==6 and dia>=1 and dia <=21:
    print('GEMINIS')
if mes==6 and dia>21 and dia<=30 or mes==7 and dia>=1 and dia <=23:
    print('CANCER')
if mes==7 and dia>23 and dia<=31 or mes==8 and dia>=1 and dia <=23:
    print('LEO')
if mes==8 and dia>23 and dia<=31 or mes==9 and dia>=1 and dia <=23:
    print('VIRGO')
if mes==9 and dia>23 and dia<=30 or mes==10 and dia>=1 and dia <=23:
    print('LIBRA')
if mes==10 and dia>23 and dia<=31 or mes==11 and dia>=1 and dia <=22:
    print('ESCORPIO')
if mes==11 and dia>22 and dia<=30 or mes==12 and dia>=1 and dia <=22:
    print('SAGITARIO')
if mes==12 and dia>22 and dia<=31 or mes==1 and dia>=1 and dia <=20:
    print('CAPRICORNIO')
if mes==1 and dia>=21 and dia<=30 or mes==2 and dia>=1 and dia <=19:
    print('ACUARIO')
if mes==2 and dia>=20 and dia<=28 or mes==3 and dia>=1 and dia <=21:
    print('PISCIS')      