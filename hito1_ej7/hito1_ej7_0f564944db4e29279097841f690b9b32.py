#Zodiaco
dia=int(input('Ingrese dia de su cumpleaños:'))
mes=int(input('Ingrese el numero asignado al mes de su cumpleaños:'))
if mes==1:
    if dia>=1 and dia<=20:
        print('Capricornio')
    elif dia>=21 and dia<=31:
        print('Acuario')
    else:
        print('Digito numeros fuera de rango')
elif mes==2:
    if dia>=1 and dia<=19:
        print('Acuario')
    elif dia>=20 and dia<=28:
        print('Piscis')
    else:
        print('Digito numeros fuera de rango')
elif mes==3:
    if dia>=1 and dia<=20:
        print('Piscis')
    elif dia>=21 and dia<=31:
        print('Aries')
    else:
        print('Digito numeros fuera de rango')
elif mes==4:
    if dia>=1 and dia<=20:
        print('Aries')
    elif dia>=21 and dia<=30:
        print('Tauro')
    else:
        print('Digito numeros fuera de rango')
elif mes==5:
    if dia>=1 and dia<=21:
        print('Tauro')
    elif dia>=22 and dia<=31:
        print('Geminis')
    else:
        print('Digito numeros fuera de rango')
elif mes==6:
    if dia>=1 and dia<=21:
        print('Geminis')
    elif dia>=22 and dia<=30:
        print('Cancer')
    else:
        print('Digito numeros fuera de rango')
elif mes==7:
    if dia>=1 and dia<=22:
        print('Cancer')
    elif dia>=23 and dia<=31:
        print('Leo')
    else:
        print('Digito numeros fuera de rango')
elif mes==8:
    if dia>=1 and dia<=22:
        print('Leo')
    elif dia>=23 and dia<=31:
        print('Virgo')
    else:
        print('Digito numeros fuera de rango')
elif mes==9:
    if dia>=1 and dia<=23:
        print('Virgo')
    elif dia>=24 and dia<=30:
        print('Libra')
    else:
        print('Digito numeros fuera de rango')
elif mes==10:
    if dia>=1 and dia<=23:
        print('Libra')
    elif dia>=24 and dia<=31:
        print('Escorpion')
    else:
        print('Digito numeros fuera de rango')
elif mes==11:
    if dia>=1 and dia<=22:
        print('Escorpion')
    elif dia>=23 and dia<=30:
        print('Sagitario')
    else:
        print('Digito numeros fuera de rango')
elif mes==12:
    if dia>=1 and dia<=21:
        print('Sagitario')
    elif dia>=22 and dia<=31:
        print('Capricornio')
    else:
        print('Digito numeros fuera de rango')
else:
    print('Digito numeros fuera de rango')     