def signo_zodiacal(dia, mes):
    if mes == 12:
        signo = 'Sagitario' if (dia < 22) else 'Capricornio'
    elif mes == 1:
        signo = 'Capricornio' if (dia < 20) else 'Acuario'
    elif mes == 2:
        signo = 'Acuario' if (dia < 19) else 'Piscis'
    elif mes == 3:
        signo = 'Piscis' if (dia < 21) else 'Aries'
    elif mes == 4:
        signo = 'Aries' if (dia < 20) else 'Tauro'
    elif mes == 5:
        signo = 'Tauro' if (dia < 21) else 'Géminis'
    elif mes == 6:
        signo = 'Géminis' if (dia < 21) else 'Cáncer'
    elif mes == 7:
        signo = 'Cáncer' if (dia < 23) else 'Leo'
    elif mes == 8:
        signo = 'Leo' if (dia < 23) else 'Virgo'
    elif mes == 9:
        signo = 'Virgo' if (dia < 23) else 'Libra'
    elif mes == 10:
        signo = 'Libra' if (dia < 23) else 'Escorpio'
    elif mes == 11:
        signo = 'Escorpio' if (dia < 22) else 'Sagitario'

    return signo

dia = int(input("Día: "))
mes = int(input("Mes: "))
print(signo_zodiacal(dia,mes))