#ZoVal_diaco

#Registro Valores a Consultar
Val_dia = int(input('Indique  día: '))
Val_mes = int(input('Indique  mes: '))

if Val_mes == 12 and Val_dia > 22 or Val_mes == 1 and Val_dia <= 20:
    print('Su signo es: Capricornio')
elif Val_mes == 1 and Val_dia > 20 or Val_mes == 2 and Val_dia <= 19:
    print('Su signo es: Acuario')
elif Val_mes == 2 and Val_dia > 19 or Val_mes == 3 and Val_dia <= 21:
    print('Su signo es: Pisis')
elif Val_mes == 3 and Val_dia < 21 or Val_mes == 4 and Val_dia <= 20:
    print('Su signo es: Aries')
elif Val_mes == 4 and Val_dia < 20 or Val_mes == 5 and Val_dia <= 21:
    print('Su signo es: Tauro')
elif Val_mes == 5 and Val_dia < 21 or Val_mes == 6 and Val_dia <= 21:
    print('Su signo es: Geminis')
elif Val_mes == 6 and Val_dia < 21 or Val_mes == 7 and Val_dia <= 21:
    print('Su signo es: Cancer')
elif Val_mes == 7 and Val_dia < 23 or Val_mes == 8 and Val_dia <= 23:
    print('Su signo es: Leo')
elif Val_mes == 8 and Val_dia < 23 or Val_mes == 9 and Val_dia <= 23:
    print('Su signo es: Virgo')
elif Val_mes == 9 and Val_dia < 23 or Val_mes == 10 and Val_dia <= 23:
    print('Su signo es: Libra')
elif Val_mes == 10 and Val_dia < 23 or Val_mes == 11 and Val_dia <= 22:
    print('Su signo es: Escorpion')
elif Val_mes == 11 and Val_dia < 22 or Val_mes == 12 and Val_dia <= 22:
    print('Su signo es: Sagitario')
      