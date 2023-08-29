def determinar_signo(dia, mes):
    if (mes == 1 and 20 <= dia and dia <= 31) or (mes == 2 and 1 <= dia and dia <= 18):
        return "Acuario"
    elif (mes == 2 and 19 <= dia and dia <= 29) or (mes == 3 and 1 <= dia and dia <= 20):
        return "Piscis"
    elif (mes == 3 and 21 <= dia and dia <= 31) or (mes == 4 and 1 <= dia and dia <= 19):
        return "Aries"
    elif (mes == 4 and 20 <= dia and dia <= 30) or (mes == 5 and 1 <= dia and dia <= 20):
        return "Tauro"
    elif (mes == 5 and 21 <= dia and dia <= 31) or (mes == 6 and 1 <= dia and dia <= 20):
        return "Géminis"
    elif (mes == 6 and 21 <= dia and dia <= 30) or (mes == 7 and 1 <= dia and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and 23 <= dia and dia <= 31) or (mes == 8 and 1 <= dia and dia <= 22):
        return "Leo"
    elif (mes == 8 and 23 <= dia and dia <= 31) or (mes == 9 and 1 <= dia and dia <= 22):
        return "Virgo"
    elif (mes == 9 and 23 <= dia and dia <= 30) or (mes == 10 and 1 <= dia and dia <= 22):
        return "Libra"
    elif (mes == 10 and 23 <= dia and dia <= 31) or (mes == 11 and 1 <= dia and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and 22 <= dia and dia <= 30) or (mes == 12 and 1 <= dia and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and 22 <= dia and dia <= 31) or (mes == 1 and 1 <= dia and dia <= 19):
        return "Capricornio"
    else:
        return "Fecha inválida"

dia = int(input("Ingrese el día de su cumpleaños: "))
mes = int(input("Ingrese el mes de su cumpleaños: "))

signo_zodiaco = determinar_signo(dia, mes)

print("Su signo del zodíaco es:", signo_zodiaco)