def determinar_signo_zodiaco(dia, mes):
    signos_zodiaco = {
        "Aries": ((3, 21), (4, 20)),
        "Tauro": ((4, 21), (5, 20)),
        "Géminis": ((5, 21), (6, 20)),
        "Cáncer": ((6, 21), (7, 22)),
        "Leo": ((7, 23), (8, 22)),
        "Virgo": ((8, 23), (9, 22)),
        "Libra": ((9, 23), (10, 22)),
        "Escorpio": ((10, 23), (11, 22)),
        "Sagitario": ((11, 23), (12, 22)),
        "Capricornio": ((12, 22), (1, 20)),
        "Acuario": ((1, 21), (2, 19)),
        "Piscis": ((2, 20), (3, 20))
    fecha = (dia, mes)
    for signo, fechas in signos_zodiaco.items():
        if fecha >= fechas[0] and fecha <= fechas[1]:
            return signo
    return "Fecha no válida"

# Solicitar al usuario que ingrese el día y mes de su cumpleaños
dia = int(input("Ingresa el día de tu cumpleaños (número entero): "))
mes = int(input("Ingresa el mes de tu cumpleaños (número entero): "))

# Determinar el signo del zodíaco
signo = determinar_signo_zodiaco(dia, mes)

# Imprimir el resultado
print("Tu signo del zodíaco es:", signo)