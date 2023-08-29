def obtener_signo(zodiaco):
    signos = [
        (1, 20, "Acuario", "Piscis"),
        (2, 19, "Piscis", "Aries"),
        (3, 21, "Aries", "Tauro"),
        (4, 20, "Tauro", "Géminis"),
        (5, 21, "Géminis", "Cáncer"),
        (6, 21, "Cáncer", "Leo"),
        (7, 23, "Leo", "Virgo"),
        (8, 23, "Virgo", "Libra"),
        (9, 23, "Libra", "Escorpio"),
        (10, 23, "Escorpio", "Sagitario"),
        (11, 22, "Sagitario", "Capricornio"),
        (12, 22, "Capricornio", "Acuario")
    ]
    for i in range(len(signos)):
        mes_inicio, dia_inicio, signo_actual, signo_siguiente = signos[i]
        mes_siguiente, dia_siguiente, _, _ = signos[(i + 1) % len(signos)]
        if (zodiaco[0] == mes_inicio and zodiaco[1] >= dia_inicio) or \
           (zodiaco[0] == mes_siguiente and zodiaco[1] < dia_siguiente):
            return signo_actual
    return ""

def obtener_fecha():
    while True:
        try:
            dia = int(input("Ingresa el día de tu cumpleaños: "))
            mes = int(input("Ingresa el mes de tu cumpleaños: "))
            if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12:
                return (mes, dia)
            else:
                print("Fecha inválida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

fecha_cumple = obtener_fecha()
signo = obtener_signo(fecha_cumple)
if signo:
    print("Tu signo zodiacal es:", signo)
else:
    print("No se pudo determinar tu signo zodiacal.")
      