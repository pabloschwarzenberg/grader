#Zodiaco
def obtener_signo(dia_nacimiento, mes_nacimiento):
    signo = ""
    if mes_nacimiento == 1:
        if dia_nacimiento <= 20:
            signo = "Capricornio"
        else:
            signo = "Acuario"
    elif mes_nacimiento == 2:
        if dia_nacimiento <= 18:
            signo = "Acuario"
        else:
            signo = "Piscis"
    elif mes_nacimiento == 3:
        if dia_nacimiento <= 20:
            signo = "Piscis"
        else:
            signo = "Aries"
    elif mes_nacimiento == 4:
        if dia_nacimiento <= 20:
            signo = "Aries"
        else:
            signo = "Tauro"
    elif mes_nacimiento == 5:
        if dia_nacimiento <= 21:
            signo = "Tauro"
        else:
            signo = "Géminis"
    elif mes_nacimiento == 6:
        if dia_nacimiento <= 21:
            signo = "Géminis"
        else:
            signo = "Cancer"
    elif mes_nacimiento == 7:
        if dia_nacimiento <= 22:
            signo = "Cáncer"
        else:
            signo = "Leo"
    elif mes_nacimiento == 8:
        if dia_nacimiento <= 23:
            signo = "Leo"
        else:
            signo = "Virgo"
    elif mes_nacimiento == 9:
        if dia_nacimiento <= 23:
            signo = "Virgo"
        else:
            signo = "Libra"
    elif mes_nacimiento == 10:
        if dia_nacimiento <= 23:
            signo = "Libra"
        else:
            signo = "Escorpio"
    elif mes_nacimiento == 11:
        if dia_nacimiento <= 22:
            signo = "Escorpio"
        else:
            signo = "Sagitario"
    elif mes_nacimiento == 12:
        if dia_nacimiento <= 21:
            signo = "Sagitario"
        else:
            signo = "Capricornio"
    return signo

dia = int(input("Ingresa tu día de nacimiento [1-31]: "))
mes = int(input("Ingresa tu mes de nacimiento [1-12]: "))

signo = obtener_signo(dia, mes)
print(signo)      