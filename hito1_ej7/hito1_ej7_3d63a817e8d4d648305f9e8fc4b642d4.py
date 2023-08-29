#Zodiaco
#Entrada

dia = int(input("ingrese su día de nacimiento: "))
mes = int(input("ingrese su mes de nacimiento: "))

if mes == 1:
    if 31 >= dia >= 20:
        print("Su signo del zodiaco es 'acuario'")
    elif dia < 20:
        print("Su signo del zodiaco es 'capricornio'")
    else:
        print("El día ingresado no es válido")
elif mes == 2:
    if 29 >= dia >= 19 :
        print("Su signo del zodiaco es 'piscis'")
    elif dia < 20:
        print("Su signo del zodiaco es 'acuario'")
    else:
        print("El día ingresado no es válido")
elif mes == 3:
    if 31 >= dia >= 21:
        print("Su signo del zodiaco es 'aries'")
    elif dia < 21:
        print("Su signo del zodiaco es 'piscis'")
    else:
        print("El día ingresado no es válido")
elif mes == 4 <= 30:
    if 30 >= dia >= 20:
        print("Su signo del zodiaco es 'tauro'")
    elif dia < 20:
        print("Su signo del zodiaco es 'aries'")
    else:
        print("El día ingresado no es válido")
elif mes == 5:
    if 31 >= dia >= 21 <= 31:
        print("Su signo del zodiaco es 'geminis'")
    elif dia < 21:
        print("Su signo del zodiaco es 'tauro'")
    else:
        print("El día ingresado no es válido")
elif mes == 6:
    if 30 >= dia >= 21:
        print("Su signo del zodiaco es 'cáncer'")
    elif dia < 21:
        print("Su signo del zodiaco es 'geminis'")
    else:
        print("El día ingresado no es válido")
elif mes == 7:
    if 31 >= dia >= 23:
        print("Su signo del zodiaco es 'leo'")
    elif dia < 21:
        print("Su signo del zodiaco es 'cáncer'")
    else:
        print("El día ingresado no es válido")
elif mes == 8:
    if 31 >= dia >= 23:
        print("Su signo del zodiaco es 'virgo'")
    elif dia < 23:
        print("Su signo del zodiaco es 'leo'")
    else:
        print("El día ingresado no es válido")
elif mes == 9:
    if 30>= dia >= 23:
        print("Su signo del zodiaco es 'libra'")
    elif dia < 23:
        print("Su signo del zodiaco es 'virgo'")
    else:
        print("El día ingresado no es válido")
elif mes == 10:
    if 31 >= dia >= 23:
        print("Su signo del zodiaco es 'escorpio'")
    elif dia < 23:
        print("Su signo del zodiaco es 'libra'")
    else:
        print("El día ingresado no es válido")
elif mes == 11:
    if 30 >= dia >= 23:
        print("Su signo del zodiaco es 'sagitario'")
    elif dia < 23:
        print("Su signo del zodiaco es 'escorpio'")
    else:
        print("El día ingresado no es válido")
elif mes == 12:
    if 31 >= dia >= 22:
        print("Su signo del zodiaco es 'capricornio'")
    elif dia < 22:
        print("Su signo del zodiaco es 'sagitario'")
    else:
        print("El día ingresado no es válido")
else:
    print("el mes ingresado no es válido.")