def signo_zodiacal(dia, mes):
    if mes == 1:
        return 'Capricornio' if dia <= 19 else 'Acuario'
    elif mes == 2:
        return 'Acuario' if dia <= 18 else 'Piscis'
    elif mes == 3:
        return 'Piscis' if dia <= 20 else 'Aries'
    elif mes == 4:
        return 'Aries' if dia <= 19 else 'Tauro'
    elif mes == 5:
        return 'Tauro' if dia <= 20 else 'Géminis'
    elif mes == 6:
        return 'Géminis' if dia <= 20 else 'Cáncer'
    elif mes == 7:
        return 'Cáncer' if dia <= 22 else 'Leo'
    elif mes == 8:
        return 'Leo' if dia <= 22 else 'Virgo'
    elif mes == 9:
        return 'Virgo' if dia <= 22 else 'Libra'
    elif mes == 10:
        return 'Libra' if dia <= 22 else 'Escorpio'
    elif mes == 11:
        return 'Escorpio' if dia <= 21 else 'escorpio'
    elif mes == 12:
        return 'Sagitario' if dia <= 21 else 'Capricornio'


dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
signo = signo_zodiacal(dia, mes)
print("El signo zodiacal de la persona es", signo)
