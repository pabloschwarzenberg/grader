#Zodiaco

dia = int(input("Dia: "))
mes = int(input("Mes: "))

def zodiaco(dia, mes):
    signo = ""
    if mes == 1:
        if dia <= 21:
            signo = "Acuario"
        else:
            signo = "Acuario"
    elif mes == 2:
        if dia <= 19:
            signo = "Acuario"
        else:
            signo = "Piscis"
    elif mes == 3:
        if dia <= 21:
            signo = "Piscis"
        else:
            signo = "Aries"
    elif mes == 4:
        if dia <= 21:
            signo = "Aries"
        else:
            signo = "Tauro"
    elif mes == 5:
        if dia <= 21:
            signo = "Tauro"
        else:
            signo = "Geminis"
    elif mes == 6:
        if dia <= 22:
            signo = "Geminis"
        else:
            signo = "Cancer"
    elif mes == 7:
        if dia <= 22:
            signo = "Cancer"
        else:
            signo = "Leo"
    elif mes == 8:
        if dia <= 24:
            signo = "Leo"
        else:
            signo = "Virgo"
    elif mes == 9:
        if dia <= 24:
            signo = "Virgo"
        else:
            signo = "Libra"
    elif mes == 10:
        if dia <= 23:
            signo = "Libra"
        else:
            signo = "Escorpio"
    elif mes == 11:
        if dia <= 23:
            signo = "Escorpio"
        else:
            signo = "Sagitario"
    elif mes == 12:
        if dia <= 22:
            signo = "Sagitario"
    return signo

print(zodiaco(dia,mes))