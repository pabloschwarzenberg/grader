dia = int(input("Ingrese su día de nacimiento [1-31]: "))
mes = int(input("Ingrese su mes de nacimiento [1-12]: "))

def obtener_signo(dia, mes):
    signo = (" ")

    if mes == 1:
        if dia <= 20:
            signo = "capricornio"
        else:
            signo = "acuario"

    elif mes == 2:
        if dia <= 19:
            signo = "acuario"
        else:
            signo = "piscis"

    elif mes == 3:
        if dia <= 21:
            signo = "piscis"
        else:
            signo = "aries"

    elif mes == 4:
        if dia <= 20:
            signo = "aries"
        else:
            signo = "tauro"

    elif mes == 5:
        if dia <= 21:
            signo = "tauro"
        else:
            signo = "geminis"

    elif mes == 6:
        if dia <= 21:
            signo = "geminis"
        else:
            signo = "cancer"

    elif mes == 7:
        if dia <= 23:
            signo = "cancer"
        else:
            signo = "leo"

    elif mes == 8:
        if dia <= 23:
            signo = "leo"
        else:
            signo = "virgo"

    elif mes == 9:
        if dia <= 23:
            signo = "virgo"
        else:
            signo = "libra"

    elif mes == 10:
        if dia <= 23:
            signo = "libra"
        else:
            signo = "escorpio"

    elif mes == 11:
        if dia <= 22:
            signo = "escorpio"
        else:
            signo = "sagitario"

    elif mes == 12:
        if dia <= 22:
            signo = "sagitario"
        else:
            signo = "capricornio"

    return signo

signo = obtener_signo(dia, mes)

print ("Tu signo es: ", signo)