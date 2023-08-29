#Zodiaco
dia=int(input('Ingrese el dia de su cumpleaños: '))
mes=int(input('Ingrese el mes de su cumpleaños: '))

if mes==11:
    if 1<=dia<=22:
        print('Escorpio')
    elif 23<=dia<=30:
        print('Sagitario')
elif mes==12:
    if 1<=dia<=22:
        print('Sagitario')
    elif 23<=dia<=31:
        print('Capricornio')
elif mes==1:
    if 1<=dia<=20:
        print('Capricornio')
    elif 21<=dia<=30:
        print('Acuario')
elif mes==2:
    if 1<=dia<=19:
        print('Acuario')
    elif 20<=dia<=29:
        print('Piscis')
elif mes==3:
    if 1<=dia<=21:
        print('Piscis')
    elif 22<=dia<=31:
        print('Aries')
elif mes==4:
    if 1<=dia<=20:
        print('Aries')
    elif 21<=dia<=30:
        print('Tauro')
elif mes==5:
    if 1<=dia<=21:
        print('Tauro')
    elif 22<=dia<=31:
        print('Géminis')
elif mes==6:
    if 1<=dia<=21:
        print('Géminis')
    elif 22<=dia<=30:
        print('Cáncer')
elif mes==7:
    if 1<=dia<=23:
        print('Cáncer')
    elif 24<=dia<=31:
        print('Leo')
elif mes==8:
    if 1<=dia<=23:
        print('Leo')
    elif 24<=dia<=31:
        print('Virgo')
elif mes==9:
    if 1<=dia<=23:
        print('Virgo')
    elif 24<=dia<=30:
        print('Libra')
elif mes==10:
    if 1<=dia<=23:
        print('Libra')
    elif 24<=dia<=31:
        print('Escorpio')
elif dia==0 or dia>31 or mes==0 or mes>12:
    print('Ingrese un dia o un mes validos')