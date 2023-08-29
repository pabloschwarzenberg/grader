#Zodiaco
x=int(input('ingrese el dia en que nacio:'))
y=int(input('ingrese el numero del mes en que nacio:'))
if 1<=x<=31:
    if y==1:
        if 1<=x<20:
            print('CAPRICORNIO')
        else:
            print('ACUARIO')
    elif y==2:
        if 1<=x<19:
            print('ACUARIO')
        else:
            print('PISCIS')
    elif y==3:
        if 1<=x<21:
            print('PISCIS')
        else:
            print('ARIES')
    elif y==4:
        if 1<=x<20:
            print('ARIES')
        else:
            print('TAURO')
    elif y==5:
        if 1<=x<21:
            print('TAURO')
        else:
            print('GEMINI')
    elif y==6:
        if 1<=x<21:
            print('GEMINI')
        else:
            print('CANCER')
    elif y==7:
        if 1<=x<23:
            print('CANCER')
        else:
            print('LEO')
    elif y==8:
        if 1<=x<23:
            print('LEO')
        else:
            print('VIRGO')
    elif y==9:
        if 1<=x<23:
            print('VIRGO')
        else:
            print('LIBRA')
    elif y==10:
        if 1<=x<23:
            print('LIBRA')
        else:
            print('SCORPIO')
    elif y==11:
        if 1<=x<22:
            print('SCORPIO')
        else:
            print('SAGITARIO')
    elif y==12:
        if 1<=x<22:
            print('SAGITARIO')
        else:
            print('CAPRICORNIO')
    else:
        print('ERROR')
else:
    print('ERROR')
             
                   