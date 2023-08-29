#Zodiaco
dia=int(input('ingrese su dia de nacimiento: '))
mes=int(input('ingrese su mes de nacimiento en numero: '))

if dia>=20 and dia<31 and mes==1 or mes==2 and dia<=19:
    print('Usted es Acuario')

if dia>19 and dia<31 and mes==2 or mes==3 and dia<=21:
    print('Usted es Piscis')

if dia>21 and dia<31 and mes==3 or mes==4 and dia<=20:
    print('Usted es Aries')

if dia>20 and dia<31 and mes==4 or mes==5 and dia<=21:
    print('Usted es Tauro')

if dia>21 and dia<31 and mes==5 or mes==6 and dia<=21:
    print('Usted es Gemini')

if dia>21 and dia<31 and mes==6 or mes==7 and dia<=23:
    print('Usted es Cancer')

elif dia>23 and dia<31 and mes==7 or mes==8 and dia<=23:
    print('Usted es Leo')

if dia>23 and dia<31 and mes==8 or mes==9 and dia<=23:
    print('Usted es Virgo')

elif dia>23 and dia<31 and mes==9 or mes==10 and dia<=23:
    print('Usted es Libra')

if dia>23 and dia<31 and mes==10 or mes==11 and dia<=22:
    print('Usted es Escorpion')

if dia>22 and dia<31 and mes==11 or mes==12 and dia<=22:
    print('Usted es Sagitario')

if dia>22 and dia<12 and mes==1 or mes==1 and dia<=20:
    print('Usted es Capricornio')    
     