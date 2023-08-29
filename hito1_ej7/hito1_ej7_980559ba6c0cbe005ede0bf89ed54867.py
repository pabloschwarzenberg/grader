#Zodiaco
d = int(input('Ingrese el dia: '))
m = int(input('Ingrese el mes: '))

if m == 1:
    if d <= 20:
        print('Capricornio')
    elif d >= 21:
        print('Aquarius')
elif m == 2:
    if d <= 21:
        print('Aquarius')
    elif d >= 20:
        print('Piscis')
elif m == 3:
    if d <= 20:
        print('Piscis')
    elif d >= 21:
        print('Aries')
elif m == 4:
    if d <= 20:
        print('Aries')
    elif d >= 21:
        print('Tauro')
elif m == 5:
    if d <= 20:
        print('Tauro')
    elif d >= 21:
        print('Geminis')
elif m == 6:
    if d <= 21:
        print('Geminis')
    elif d >= 22:
        print('Cancer')
elif m == 7:
    if d <= 21:
        print('Cancer')
    elif d >= 22:
        print('Leo')
elif m == 8:
    if d <= 23:
        print('Leo')
    elif d >= 24:
        print('Virgo')
elif m == 9:
    if d <= 23:
        print('Virgo')
    elif d >= 24:
        print('Libra')
elif m == 10:
    if d <= 22:
        print('Libra')
    elif d >= 23:
        print('Escorpio')
elif m == 11:
    if d <= 22:
        print('Escorpio')
    elif d >= 23:
        print('Sagitario')
elif m == 12:
    if d <= 21:
        print('Sagitario')
    elif d >= 22:
        print('Capricornio')          