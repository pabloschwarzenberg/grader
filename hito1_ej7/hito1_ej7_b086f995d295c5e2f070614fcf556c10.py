def obtener_signo_zodiacal(dia, mes):
    signos_zodiacales = [("Capricornio", 1, 19), ("Acuario", 1, 20), ("Piscis", 2, 19), ("Aries", 3, 21), ("Tauro", 4, 20), ("Géminis", 5, 21), ("Cáncer", 6, 21), ("Leo", 7, 23), ("Virgo", 8, 23), ("Libra", 9, 23), ("Escorpio", 10, 23), ("Sagitario", 11, 22), ("Capricornio", 12, 22)]
    if (mes == signos_zodiacales[0][1] and dia < signos_zodiacales[0][2]) or (mes == signos_zodiacales[-1][1] and dia >= signos_zodiacales[-1][2]):
        return signos_zodiacales[-1][0]
    for i in range(len(signos_zodiacales)-1):
        if (mes == signos_zodiacales[i][1] and dia >= signos_zodiacales[i][2]) or (mes == signos_zodiacales[i+1][1] and dia < signos_zodiacales[i+1][2]):
            return signos_zodiacales[i][0]
            
dia = int(input("Ingresa el día de tu nacimiento: "))
mes = int(input("Ingresa el mes de tu nacimiento: "))

signo = obtener_signo_zodiacal(dia, mes)

print("Tu signo zodiacal es:", signo)