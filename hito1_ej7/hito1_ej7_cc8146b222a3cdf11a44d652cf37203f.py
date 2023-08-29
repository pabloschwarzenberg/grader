def obtener_signo_zodiaco(dia, mes):

    if (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        "Acuario"
        return "Acuario"
    elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 20):
        "Piscis"
        return "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        "Aries"
        return "Aries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        "Tauro"
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        "Géminis"
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        "Cáncer"
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
        "Leo"
        return "Leo"
    elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 22):
        "Virgo"
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        "Libra"
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        "Escorpio"
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 20):
        "Sagitario"
        return "Sagitario"
    else:
        return "Capricornio"

dia = int(input("Ingresa el día de tu cumpleaños: "))
mes = int(input("Ingresa el mes de tu cumpleaños: "))

signo = obtener_signo_zodiaco(dia, mes)
print("Tu signo zodiacal es:", signo)
