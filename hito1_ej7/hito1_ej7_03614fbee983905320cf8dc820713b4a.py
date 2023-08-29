#Zodiaco
dia=int(input('Ingresa tu dia de nacimiento: '))
mes=int(input('Ingresa tu mes de nacimiento: '))

if(mes==3 and dia -21 >=0 and dia <=31) or (mes==4 and dia <=20 and dia >= 1):
    print ('ARIES')

if(mes==4 and dia -21 >=0 and dia <=31) or (mes==5 and dia <=20 and dia >= 1):
    print ('TAURO')

if(mes==5 and dia -21 >=0 and dia <=31) or (mes==6 and dia <=20 and dia >= 1):
    print ('GEMINIS')

if(mes==6 and dia -21 >=0 and dia <=31) or (mes==7 and dia <=23 and dia >= 1):
    print ('CANCER')

if(mes==7 and dia -23 >=0 and dia <=31) or (mes==8 and dia <=23 and dia >= 1):
    print ('LEO')

if(mes==8 and dia -23 >=0 and dia <=31) or (mes==9 and dia <=23 and dia >= 1):
    print ('VIRGO')

if(mes==9 and dia -23 >=0 and dia <=31) or (mes==10 and dia <=23 and dia >= 1):
    print ('LIBRA')

if(mes==10 and dia -23 >=0 and dia <=31) or (mes==11 and dia <=22 and dia >= 1):
    print ('ESCORPIO')

if(mes==11 and dia -22 >=0 and dia <=31) or (mes==12 and dia <=22 and dia >= 1):
    print ('SAGITARIO')

if(mes==12 and dia -22 >=0 and dia <=31) or (mes==1 and dia <=20 and dia >= 1):
    print ('CAPRICORNIO')

if(mes==1 and dia -20 >=0 and dia <=31) or (mes==2 and dia <=19 and dia >= 1):
    print ('ACUARIO')

if(mes==2 and dia -19 >=0 and dia <=31) or (mes==3 and dia <=21 and dia >= 1):
    print ('PISCIS')      