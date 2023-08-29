#Zodiaco
F=int(input('ingrese el número del día en que nació: '))
M=int(input('ingrese el número del mes en el que nació: '))
if (F>=21 and F<=31 and M==3) or (F>=1 and F<=20 and M==4):
    print('su signo del zodiaco es aries')
elif (F>=21 and F<=31 and M==4) or (F>=1 and F<=21 and M==5):
    print('su signo del zodiaco es tauro')
elif (F>=22 and F<=31 and M==5) or (F>=1 and F<=21 and M==6):
    print('su signo del zodiaco es geminis')
elif (F>=22 and F<=31 and M==6) or (F>=1 and F<=22 and M==7):
    print('su signo del zodiaco es cancer')
elif(F>=23 and F<=31 and M==7) or (F>=1 and F<=22 and M==8):
    print('su signo del zodiaco es leo')
elif (F>=23 and F<=31 and M==8) or (F>=1 and F<=23 and M==9):
    print('su signo del zodiaco es virgo')
elif (F>=24 and F<=31 and M==9) or (F>=1 and F<=23 and M==10):
    print('su signo del zodiaco es libra')
elif (F>=24 and F<=31 and M==10) or (F>=1 and F<=22 and M==11):
    print('su signo del zodiaco es escorpion')
elif (F>=23 and F<=31 and M==11) or (F>=1 and F<=21 and M==12):
    print('su signo del zodiaco es sagitario')
elif (F>=22 and F<=31 and M==12) or (F>=1 and F<=20 and M==1):
    print('su signo del zodiaco es capricornio')
elif (F>=21 and F<=31 and M==1) or (F>=1 and F<=19 and M==2):
    print('su signo del zodiaco es acuario')
elif (F>=20 and F<=31 and M==2) or (F>=1 and F<=20 and M==3):
    print('su signo del zodiaco es picis')
else:
    print('la fecha ingresada no es válidad, por favor intente nuevamente')