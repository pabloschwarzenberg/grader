def obtener_signo_zodiaco(dia_cumple, mes_cumple):
    if (mes_cumple == 1 and dia_cumple >= 20) or (mes_cumple == 2 and dia_cumple <= 18):
        return "Acuario"
    elif (mes_cumple == 2 and dia_cumple >= 19) or (mes_cumple == 3 and dia_cumple <= 20):
        return "Piscis"
    elif (mes_cumple == 3 and dia_cumple >= 21) or (mes_cumple == 4 and dia_cumple <= 19):
        return "Aries"
    elif (mes_cumple == 4 and dia_cumple >= 20) or (mes_cumple == 5 and dia_cumple <= 20):
        return "Tauro"
    elif (mes_cumple == 5 and dia_cumple >= 21) or (mes_cumple == 6 and dia_cumple <= 20):
        return "Géminis"
    elif (mes_cumple == 6 and dia_cumple >= 21) or (mes_cumple == 7 and dia_cumple <= 22):
        return "Cáncer"
    elif (mes_cumple == 7 and dia_cumple >= 23) or (mes_cumple == 8 and dia_cumple <= 22):
        return "Leo"
    elif (mes_cumple == 8 and dia_cumple >= 23) or (mes_cumple == 9 and dia_cumple <= 22):
        return "Virgo"
    elif (mes_cumple == 9 and dia_cumple >= 23) or (mes_cumple == 10 and dia_cumple <= 22):
        return "Libra"
    elif (mes_cumple == 10 and dia_cumple >= 23) or (mes_cumple == 11 and dia_cumple <= 21):
        return "Escorpio"
    elif (mes_cumple == 11 and dia_cumple >= 22) or (mes_cumple == 12 and dia_cumple <= 21):
        return "Sagitario"
    else:
        return "Capricornio"

# Solicitar al usuario que ingrese el día y mes de cumpleaños
dia_cumple = int(input("Ingrese el día de cumpleaños (1-31): "))
mes_cumple = int(input("Ingrese el mes de cumpleaños (1-12): "))

# Obtener el signo del zodíaco
signo = obtener_signo_zodiaco(dia_cumple, mes_cumple)

# Imprimir el signo del zodíaco
print("El signo del zodíaco es:", signo)
