def signo_zodiacal(dia, mes):
    if mes == 1:
        return 'Capricornio' if (dia < 20) else 'Acuario'
    elif mes == 2:
        return 'Acuario' if (dia < 19) else 'Piscis'
    elif mes == 3:
        return 'Piscis' if (dia < 21) else 'Aries'
    elif mes == 4:
        return 'Aries' if (dia < 20) else 'Tauro'
    elif mes == 5:
        return 'Tauro' if (dia < 21) else 'Géminis'
    elif mes == 6:
        return 'Géminis' if (dia < 21) else 'Cáncer'
    elif mes == 7:
        return 'Cáncer' if (dia < 23) else 'Leo'
    elif mes == 8:
        return 'Leo' if (dia < 23) else 'Virgo'
    elif mes == 9:
        return 'Virgo' if (dia < 23) else 'Libra'
    elif mes == 10:
        return 'Libra' if (dia < 23) else 'Escorpio'
    elif mes == 11:
        return 'Escorpio' if (dia < 22) else 'Sagitario'
    elif mes == 12:
        return 'Sagitario' if (dia < 22) else 'Capricornio'

print(signo_zodiacal(15,3)) # Output: Piscis