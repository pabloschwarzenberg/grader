#Zodiaco
def obtener_signo_zodiaco(dia, mes):
    signos_zodiaco = [
        (1, 20, "Capricornio"),
        (2, 18, "Acuario"),
        (3, 20, "Piscis"),
        (4, 19, "Aries"),
        (5, 20, "Tauro"),
        (6, 20, "Géminis"),
        (7, 22, "Cáncer"),
        (8, 22, "Leo"),
        (9, 22, "Virgo"),
        (10, 22, "Libra"),
        (11, 21, "Escorpio"),
        (12, 21, "Sagitario"),
    ]
    
    for signo in signos_zodiaco:
        if (mes, dia) <= (signo[0], signo[1]):
            return signo[2]
    
    return "Capricornio"  # Si la fecha está después del 21 de diciembre el programa respondera que el signo es Capricornio

# Se le solicita al usuario la fecha de nacimiento
dia_nacimiento = int(input("Ingresa el día de nacimiento (1-31): "))
mes_nacimiento = int(input("Ingresa el mes de nacimiento (1-12): "))

# Obtener el signo del zodíaco
signo_zodiaco = obtener_signo_zodiaco(dia_nacimiento, mes_nacimiento)

# Imprtimir lo que seria el resultado
print("Tu signo del zodíaco es:", signo_zodiaco)
      