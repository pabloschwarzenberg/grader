def signo_zodiacal(dia, mes):
    if mes == 12:
        astro_sign = 'Sagitario' if (dia < 22) else 'Capricornio'
    elif mes == 1:
        astro_sign = 'Capricornio' if (dia < 20) else 'Acuario'
    elif mes == 2:
        astro_sign = 'Acuario' if (dia < 19) else 'Piscis'
    elif mes == 3:
        astro_sign = 'Piscis' if (dia < 21) else 'Aries'
    elif mes == 4:
        astro_sign = 'Aries' if (dia < 20) else 'Tauro'
    elif mes == 5:
        astro_sign = 'Tauro' if (dia < 21) else 'Géminis'
    elif mes == 6:
        astro_sign = 'Géminis' if (dia < 21) else 'Cáncer'
    elif mes == 7:
        astro_sign = 'Cáncer' if (dia < 23) else 'Leo'
    elif mes == 8:
        astro_sign = 'Leo' if (dia < 23) else 'Virgo'
    elif mes == 9:
        astro_sign = 'Virgo' if (dia < 23) else 'Libra'
    elif mes == 10:
        astro_sign = 'Libra' if (dia < 23) else 'Escorpio'
    elif mes == 11:
        astro_sign = 'Escorpio' if (dia < 22) else 'Sagitario'

    return astro_sign

dia = int(input("Dia: "))
mes = int(input("Mes: "))
print(signo_zodiacal(dia,mes))