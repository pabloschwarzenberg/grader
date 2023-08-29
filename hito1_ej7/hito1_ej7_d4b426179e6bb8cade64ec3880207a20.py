def obtener_signo_zodiaco(dia, mes):
    # Diccionario con los signos del zodíaco y sus fechas correspondientes
    signos = {
        (1, 20): "Acuario",
        (2, 19): "Piscis",
        (3, 21): "Aries",
        (4, 20): "Tauro",
        (5, 21): "Géminis",
        (6, 21): "Cáncer",
        (7, 23): "Leo",
        (8, 23): "Virgo",
        (9, 23): "Libra",
        (10, 23): "Escorpio",
        (11, 22): "Sagitario",
        (12, 22): "Capricornio"
    }

    # Recorrer los signos y verificar si la fecha de cumpleaños coincide con alguno de ellos
    for fecha, signo in signos.items():
        if (mes, dia) >= fecha:
            return signo

    # Si no se encuentra ningún signo correspondiente, retornar None
    return None

# Solicitar al usuario ingresar el día y mes de su cumpleaños
dia = int(input("Ingrese el día de su cumpleaños: "))
mes = int(input("Ingrese el mes de su cumpleaños: "))

# Obtener el signo del zodíaco correspondiente
signo_zodiaco = obtener_signo_zodiaco(dia, mes)

# Imprimir el resultado
if signo_zodiaco:
    print("Su signo del zodíaco es:", signo_zodiaco)
else:
    print("Fecha de cumpleaños inválida.")
      