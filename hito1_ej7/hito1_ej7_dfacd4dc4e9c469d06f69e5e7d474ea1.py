#Zodiaco
dia=int(input('Ingrese dia de cumpleaños: '))
mes=int(input('Ingrese mes de cumpleaños: '))

a=mes*100+dia
if 324<=a<=421:
    print('Aries')
elif 422<=a<=521:
    print('Tauro')
elif 422<=a<=621:
    print('Geminis')
elif 622<=a<=721:
    print('Cancer')
elif 722<=a<=822:
    print('Leo')
elif 823<=a<=921:
    print('Virgo')
elif 922<=a<=1021:
    print('Libra')
elif 1022<=a<=1122:
    print('Escorpio')
elif 1123<=a<=1221:
    print('Sagitario')
elif 1222<=a<=1231 or 101<=a<=121:
    print('Capricornio')
elif 122<=a<=221 :
    print('Acuario')
elif 222<=a<=323 :
    print('Piscis')