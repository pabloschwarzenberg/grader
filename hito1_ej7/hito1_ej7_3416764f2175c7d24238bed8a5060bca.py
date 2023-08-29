d=int(input('ingrese dia de nacimiento:'))
m=int(input('ingrese mes de nacimiento  con numeros:'))
if ((d>21 and d<=31 and m==3) or (d>=1 and d<=20 and m==4)):
    print('aries')
if ((d>20 and d<=30 and m==4) or (d>=1 and d<=21 and m==5)):
    print('tauro')
if ((d>21 and d<=31 and m==5) or (d>=1 and d<=21 and m==6)):
    print('geminis')
if ((d>21 and d<=30 and m==6) or (d>=1 and d<=23 and m==7)):
    print('cancer')
if ((d>23 and d<=31 and m==7) or (d>=1 and d<=23 and m==8)):
    print('leo')
if ((d>23 and d<=31 and m==8) or (d>=1 and d<=23 and m==9)):
    print('virgo')
if ((d>23 and d<=30 and m==9) or (d>=1 and d<=23 and m==10)):
    print('libra')
if ((d>23 and d<=31 and m==10) or (d>=1 and d<=22 and m==11)):
    print('escorpio')
if ((d>22 and d<=30 and m==11) or (d>=1 and d<=22 and m==12)):
    print('sagitario')
if ((d>22 and d<=31 and m==12) or (d>=1 and d<=20 and m==1)):
    print('capricornio')
if ((d>20 and d<=31 and m==1) or (d>=1 and d<=19 and m==2)):
    print('acuario')
if ((d>19 and d<=29 and m==2) or (d>=1 and d<=21 and m==3)):
    print('pisces')