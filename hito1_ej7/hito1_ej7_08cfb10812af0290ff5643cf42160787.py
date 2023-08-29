def zodiaco(a,b):
    dia = a
    mes = b
    if mes == 1:
        if dia <= 21:
            return "capricornio"
        else:
            return "acuario"
    if mes == 2:
        if dia <= 20:
            return "acuario"
        else:
            return "piscis"
    if mes == 3:
        if dia <= 20:
            return "piscis"
        else:
            return "aries"
    if mes == 4:
        if dia <= 21:
            return "aries"
        else:
            return "taurus"
    if mes == 5:
        if dia <= 21:
            return "taurus"
        else:
            return "geminis"
    if mes == 6:
        if dia <= 21:
            return "geminis"
        else:
            return "cancer"
    if mes == 7:
        if dia <= 22:
            return "cancer"
        else:
            return "leo"
    if mes == 8:
        if dia <= 23:
            return "leo"
        else:
            return "virgo"
    if mes == 9:
        if dia <= 23:
            return "virgo"
        else:
            return "libra"
    if mes == 10:
        if dia <= 24:
            return "libra"
        else:
            return "escorpio"
    if mes == 11:
        if dia <= 22:
            return "escorpio"
        else:
            return "sagitario"
    if mes == 12:
        if dia <= 21:
            return "sagitario"
        else:
            return "capricornio"
a = int(input(""))
b = int(input(""))
print(zodiaco(a,b))