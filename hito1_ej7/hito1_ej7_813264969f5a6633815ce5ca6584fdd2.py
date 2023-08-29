def determinar_signo(dia, mes):
    signos = [
        ("Aries", (3, 21), (4, 20)), ("Tauro", (4, 21), (5, 21)),
        ("Géminis", (5, 22), (6, 21)), ("Cáncer", (6, 22), (7, 23)),
        ("Leo", (7, 24), (8, 23)), ("Virgo", (8, 24), (9, 23)),
        ("Libra", (9, 24), (10, 23)), ("Escorpio", (10, 24), (11, 22)),
        ("Sagitario", (11, 23), (12, 22)), ("Capricornio", (12, 23), (1, 20)),
        ("Acuario", (1, 21), (2, 19)), ("Piscis", (2, 20), (3, 20))
    ]

    for signo, inicio, fin in signos:
        if (mes, dia) >= inicio and (mes, dia) <= fin:
            return signo

    return "Fecha inválida"

dia = int(input("Ingrese el día de su cumpleaños: "))
mes = int(input("Ingrese el mes de su cumpleaños: "))

signo = determinar_signo(dia, mes)
print("Su signo del zodíaco es:", signo)
