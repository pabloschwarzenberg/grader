#Zodiaco
v2=int(input('Indica el dia de nacimiento: '))
print('Indica tu mes de nacimiento el numero arabigo correspodiente.Ejemplo: Marzo=3, Abril=4,..., Noviembre=11, Diciembre=12')
v1=input('Indica el numero asociado: ' )
if v1=='1':
    if v2>=1 and v2<=20:
       print('CAPRICORNIO')
    if v2>=21 and v2<=31:
        print('ACUARIO')
elif v1=='2':
    if v2>=1 and v2<=19:
       print('ACUARIO')
    if v2>=20 and v2<=29:
        print('PISCIS')
elif v1=='3':
    if v2>=1 and v2<=20:
       print('PISCIS')
    if v2>=21 and v2<=31:
        print('ARIES')
elif v1 == '4':
    if v2>=1 and v2<=20:
       print('ARIES')
    if v2>=21 and v2<=30:
        print('TAURO')
elif v1=='5':
    if v2 >= 1 and v2 <= 21:
        print('TAURO')
    if v2 >= 22 and v2 <= 31:
        print('GEMINIS')
elif v1=='6':
    if v2 >= 1 and v2 <= 21:
        print('GEMINIS')
    if v2 >= 22 and v2 <= 30:
        print('CANCER')
elif v1=='7':
    if v2 >= 1 and v2 <= 22:
        print('CANCER')
    if v2 >= 23 and v2 <= 31:
        print('LEO')
elif v1=='8':
    if v2 >= 1 and v2 <= 22:
        print('LEO')
    if v2 >= 23 and v2 <= 31:
        print('VIRGO')
elif v1=='9':
    if v2 >= 1 and v2 <= 23:
        print('VIRGO')
    if v2 >= 24 and v2 <= 30:
        print('LIBRA')
elif v1=='10':
    if v2 >= 1 and v2 <= 23:
        print('LIBRA')
    if v2 >= 24 and v2 <= 31:
        print('ESCORPIO')
elif v1=='11':
    if (v2 >= 1 and v2 <= 22):
        print('ESCORPIO')
    if v2 >= 23 and v2 <= 30:
        print('SAGITARIO')
else:
    if v2<=12:
        if v2 >= 1 and v2 <= 21:
            print('SAGITARIO')
        if v2 >= 22 and v2 <= 31:
            print('CAPRICORNIO')
    else:
        print('Error al ingresar MES')