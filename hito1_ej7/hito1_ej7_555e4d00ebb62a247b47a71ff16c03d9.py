#Zodiaco
def determinar_signo_zodiaco(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 18):
        return "Aries"
    elif (mes == 4 and dia >= 19) or (mes == 5 and dia <= 13):
        return "Tauro"
    elif (mes == 5 and dia >= 14) or (mes == 6 and dia <= 19):
        return "Geminis"
    elif (mes == 6 and dia >= 20) or (mes == 7 and dia <= 20):
        return "Cancer"
    elif (mes == 7 and dia >= 21) or (mes == 8 and dia <= 9):
        return "Leo"
    elif (mes == 8 and dia >= 10) or (mes == 9 and dia <= 15):
        return "Virgo"
    elif (mes == 9 and dia >= 16) or (mes == 10 and dia <= 30):
        return "Libra"
    elif (mes == 10 and dia >= 31) or (mes == 11 and dia <= 22):
        return "Escorpio"
    elif (mes == 11 and dia >= 23) or (mes == 11 and dia <= 29):
        return "Ofiuco"
    elif (mes == 11 and dia >= 30) or (mes == 12 and dia <= 17):
        return "Sagitario"
    elif (mes == 12 and dia >= 18) or (mes == 1 and dia <= 18):
        return "Capricornio"
    elif (mes == 1 and dia >= 19) or (mes == 2 and dia <= 15):
        return "Acuario"
    elif (mes == 2 and dia >= 16) or (mes == 3 and dia <= 11):
        return "Piscis"
    else:
        return "Fecha invalida"

# Ejemplo de uso
dia = int(input("Ingresa el dia de tu cumpleaños: "))
mes = int(input("Ingresa el mes de tu cumpleaños: "))
signo = determinar_signo_zodiaco(dia, mes)
print("Tu signo del zodiaco es:", signo)