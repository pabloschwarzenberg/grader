#Zodiaco
dia = int(input('Ingrese el dia de su nacimiento: '))
fecha = int(input('Ingrese el dia del mes de su nacimiento: '))

if dia > 21 and fecha == 3 or dia <= 20 and fecha == 4:
    print('Su sigo es ARIES')
elif dia > 20 and fecha == 4 or dia <= 21 and fecha == 5:
    print('Su sigo es TAURO')
elif dia > 21 and fecha == 5 or dia <= 21 and fecha == 6:
    print('Su sigo es GEMINIS')
elif dia > 21 and fecha == 6 or dia <= 23 and fecha == 7:
    print('Su sigo es CANCER')
elif dia > 23 and fecha == 7 or dia <= 23 and fecha == 8:
    print('Su sigo es LEO')
elif dia > 23 and fecha == 8 or dia <= 23 and fecha == 9:
    print('Su sigo es VIRGO')
elif dia > 23 and fecha == 9 or dia <= 23 and fecha == 10:
    print('Su sigo es LIBRA')
elif dia > 23 and fecha == 10 or dia <= 22 and fecha == 11:
    print('Su sigo es ESCORPIO')
elif dia > 23 and fecha == 11 or dia <= 22 and fecha == 12:
    print('Su sigo es SAGITARIO')
elif dia > 22 and fecha == 12 or dia <= 20 and fecha == 1:
    print('Su sigo es CAPRICORNIO')
elif dia > 20 and fecha == 1 or dia <= 19 and fecha == 2:
    print('Su sigo es ACUARIO')
elif dia > 19 and fecha == 2 or dia <= 21 and fecha == 3:
    print('Su sigo es PISCIS')      