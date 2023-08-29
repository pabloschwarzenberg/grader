#Zodiaco
a=int(input('ingrese el día en que nació: '))
b=int(input('ingrese el mes en el que nació: '))
if (a>=21 and a<=31 and a==3) or (a>=1 and a<=20 and a==4):
    print('su signo del zodiaco es aries')
elif (a>=21 and a<=31 and b==4) or (a>=1 and a<=21 and b==5):
    print('su signo del zodiaco es tauro')
elif (a>=22 and a<=31 and b==5) or (a>=1 and a<=21 and b==6):
    print('su signo del zodiaco es geminis')
elif (a>=22 and a<=31 and b==6) or (a>=1 and a<=22 and b==7):
    print('su signo del zodiaco es cancer')
elif(a>=23 and a<=31 and b==7) or (a>=1 and a<=22 and b==8):
    print('su signo del zodiaco es leo')
elif (a>=23 and a<=31 and b==8) or (a>=1 and a<=23 and b==9):
    print('su signo del zodiaco es virgo')
elif (a>=24 and a<=31 and b==9) or (a>=1 and a<=23 and b==10):
    print('su signo del zodiaco es libra')
elif (a>=24 and a<=31 and b==10) or (a>=1 and a<=22 and b==11):
    print('su signo del zodiaco es escorpion')
elif (a>=23 and a<=31 and b==11) or (a>=1 and a<=21 and b==12):
    print('su signo del zodiaco es sagitario')
elif (a>=22 and a<=31 and b==12) or (a>=1 and a<=20 and b==1):
    print('su signo del zodiaco es capricornio')
elif (a>=21 and a<=31 and b==1) or (a>=1 and a<=19 and b==2):
    print('su signo del zodiaco es acuario')
elif (a>=20 and a<=31 and b==2) or (a>=1 and a<=20 and b==3):
    print('su signo del zodiaco es picis')
else:
    print('la fecha ingresada no es válidad, por favor intente nuevamente')      