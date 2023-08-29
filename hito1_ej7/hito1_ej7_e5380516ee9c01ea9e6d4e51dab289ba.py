def determinar_signo_zodiaco(dia, mes):
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

    for fecha, signo in signos.items():
        if (mes, dia) >= fecha:
            return signo

    return None

# Ejemplo de uso
dia = int(input("Ingresa el día de tu cumpleaños: "))
mes = int(input("Ingresa el mes de tu cumpleaños: "))

signo = determinar_signo_zodiaco(dia, mes)

if signo:
    print("Tu signo del zodíaco es:", signo)
else:
    print("Fecha inválida")
