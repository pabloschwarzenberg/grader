#Zodiaco
dia = int(input('Ingresa tu dia de cumpleaños: '))
mes = int(input('Ingresa tu mes de cumpleaños: '))
if dia >= 1 and dia <= 31:
    if mes >= 1 and mes <= 12:
        if mes == 3 and 21 <= dia <= 31:
            print('Aries')
        if mes == 4 and 1 <= dia <= 20:
            print('Aries')
        if mes == 4 and 21 <= dia <= 30:
            print('Tauro')
        if mes == 5 and 1 <= dia <= 21:
            print('Tauro')
        if mes == 5 and 22 <= dia <= 31:
            print('Geminis')
        if mes == 6 and 1 <= dia <= 21:
            print('Geminis')
        if mes == 6 and 22 <= dia <= 30:
            print('Cancer')
        if mes == 7 and 1 <= dia <= 23:
            print('Cancer')
        if mes == 7 and 24 <= dia <= 31:
            print('Leo')
        if mes == 8 and 1 <= dia <= 23:
            print('Leo')
        if mes == 8 and 24 <= dia <= 31:
            print('Virgo')
        if mes == 9 and 1 <= dia <= 23:
            print('Virgo')
        if mes == 9 and 24 <= dia <= 30:
            print('Libra')
        if mes == 10 and 1 <= dia <= 23:
            print('Libra')
        if mes == 10 and 24 <= dia <= 31:
            print('Escorpion')
        if mes == 11 and 1 <= dia <= 22:
            print('Escorpion')
        if mes == 11 and 23 <= dia <= 30:
            print('Sagitario')
        if mes == 12 and 1 <= dia <= 22:
            print('Sagitario')
        if mes == 12 and 23 <= dia <= 31:
            print('Capricornio')
        if mes == 1 and 1 <= dia <= 20:
            print('Capricornio')
        if mes == 1 and 21 <= dia <= 31:
            print('Acuario')
        if mes == 2 and 1 <= dia <= 19:
            print('Acuario')
        if mes == 2 and 20 <= dia <= 28:
            print('Piscis')
        if mes == 3 and 1 <= dia <= 20:
            print('Piscis')
else:
    print('La fecha esta mal escrita')