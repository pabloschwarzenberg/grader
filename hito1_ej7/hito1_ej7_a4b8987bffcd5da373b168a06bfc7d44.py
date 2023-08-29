#Zodiaco
def obtener_signo_zodiaco(dia, mes):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "geminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "sagitario"
    else:
        return "capricornio"

dia_cumpleaños = int(input("Ingrese el día de su cumpleaños: "))
mes_cumpleaños = int(input("Ingrese el mes de su cumpleaños: "))

signo = obtener_signo_zodiaco(dia_cumpleaños, mes_cumpleaños)
print("El signo del zodíaco es:", signo)
