def signo_zodiacal(dia, mes):
    if mes == 1:
        if dia < 20:
            return "Capricornio"
        else:
            return "Acuario"
    elif mes == 2:
        if dia < 19:
            return "Acuario"
        else:
            return "Piscis"
    elif mes == 3:
        if dia < 21:
            return "Piscis"
        else:
            return "Aries"
    elif mes == 4:
        if dia < 20:
            return "Aries"
        else:
            return "Tauro"
    elif mes == 5:
        if dia < 21:
            return "Tauro"
        else:
            return "Géminis"
    elif mes == 6:
        if dia < 9:
            return "Géminis"
        else:
            return "Cáncer"
    elif mes == 7:
        if dia < 23:
            return "Cáncer"
        else:
            return "Leo"
    elif mes == 8:
        if dia < 23:
            return "Leo"
        else:
            return "Virgo"
    elif mes == 9:
        if dia < 23:
            return "Virgo"
        else:
            return "Libra"
    elif mes == 10:
        if dia < 23:
            return "Libra"
        else:
            return "Escorpio"
    elif mes == 11:
        if dia < 22:
            return "Escorpio"
        else:
            return "Sagitario"
    elif mes == 12:
        if dia < 22:
            return "Sagitario"
        else:
            return "Capricornio"

print(signo_zodiacal(15,3))