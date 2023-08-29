#Zodiaco
def determinar_signo_zodiaco(dia, mes):
    signos = {
        (1, 21): "Acuario",
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

    if mes < 1 or mes > 12:
        return "Error: Mes inválido"
    
    if dia < 1 or dia > 31:
        return "Error: Día inválido"

    for fecha, signo in signos.items():
        if (mes == fecha[0] and dia >= fecha[1]) or (mes == fecha[0] + 1 and dia < fecha[1]):
            return signo

    return "Error: Fecha inválida"

# Solicitar la fecha de cumpleaños al usuario
dia = int(input("Ingrese el día de su cumpleaños (número): "))
mes = int(input("Ingrese el mes de su cumpleaños (número): "))

# Determinar el signo del zodíaco
signo_zodiaco = determinar_signo_zodiaco(dia, mes)

# Imprimir el resultado
print("Su signo del zodíaco es:", signo_zodiaco)