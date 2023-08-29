def obtener_signo_zodiaco(dia, mes):
    """
    Función para obtener el signo del zodíaco a partir del día y mes de cumpleaños.

    Argumentos:
    - dia: día de cumpleaños (número entero)
    - mes: mes de cumpleaños (número entero)

    Retorna:
    - signo: signo del zodíaco correspondiente
    """
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
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
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    else:
        return "Piscis"

# Solicitar al usuario ingresar el día y mes de cumpleaños
dia = int(input("Ingrese el día de cumpleaños: "))
mes = int(input("Ingrese el mes de cumpleaños: "))

# Obtener el signo del zodíaco
signo_zodiaco = obtener_signo_zodiaco(dia, mes)

# Mostrar el resultado
print("El signo del zodíaco es:", signo_zodiaco)


      