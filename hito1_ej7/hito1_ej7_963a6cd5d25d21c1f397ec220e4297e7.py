#Zodiaco
def determinar_signo_zodiaco(dia, mes):
    signos = [
        (1, 20, 2, 18, "Acuario"),
        (2, 19, 3, 20, "Piscis"),
        (3, 21, 4, 19, "Aries"),
        (4, 20, 5, 20, "Tauro"),
        (5, 21, 6, 20, "Geminis"),
        (6, 21, 7, 22, "Cancer"),
        (7, 23, 8, 22, "Leo"),
        (8, 23, 9, 22, "Virgo"),
        (9, 23, 10, 22, "Libra"),
        (10, 23, 11, 21, "Escorpio"),
        (11, 22, 12, 21, "Sagitario"),
        (12, 22, 1, 19, "Capricornio")
    ]

    for signo in signos:
        mes_inicio, dia_inicio, mes_fin, dia_fin, nombre = signo
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            return nombre

    return "Fecha de cumpleaños inválida"

# Obtener el día y el mes de cumpleaños del usuario
dia_cumple = int(input("Ingrese el día de su cumpleaños: "))
mes_cumple = int(input("Ingrese el mes de su cumpleaños: "))

# Determinar el signo del zodíaco
signo = determinar_signo_zodiaco(dia_cumple, mes_cumple)

# Imprimir el resultado
print("El signo del zodíaco correspondiente es:", signo)
