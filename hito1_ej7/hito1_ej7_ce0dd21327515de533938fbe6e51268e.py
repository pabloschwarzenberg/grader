def obtener_signo_zodiaco(dia, mes):
    # Lista con las fechas de inicio de cada signo zodiacal
    fechas_zodiaco = [
        (1, 20),  # Capricornio - 20 de enero
        (2, 19),  # Acuario - 19 de febrero
        (3, 21),  # Piscis - 21 de marzo
        (4, 20),  # Aries - 20 de abril
        (5, 21),  # Tauro - 21 de mayo
        (6, 21),  # Géminis - 21 de junio
        (7, 23),  # Cáncer - 23 de julio
        (8, 23),  # Leo - 23 de agosto
        (9, 23),  # Virgo - 23 de septiembre
        (10, 23),  # Libra - 23 de octubre
        (11, 22),  # Escorpio - 22 de noviembre
        (12, 22)  # Sagitario - 22 de diciembre
    ]

    # Comprobación de cada signo zodiacal
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    else:
        return "Capricornio"

# Ejemplo de uso
dia = int(input("Ingresa el día de tu cumpleaños: "))
mes = int(input("Ingresa el mes de tu cumpleaños: "))

signo = obtener_signo_zodiaco(dia, mes)
print("Tu signo del zodíaco es:", signo)
