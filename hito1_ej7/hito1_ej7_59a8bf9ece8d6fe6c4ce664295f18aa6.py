dia = int(input("Ingresa tu dia de cumpleaños: "))
mes = int(input("Ingresa tu mes de cumpleaños: "))
singo_zodiacal = " "
if mes == 12:
    signo_zodiacal = "sagitario" if (dia < 22) else "capricornio"
elif mes == 1:
    signo_zodiacal = "capricornio" if (dia < 20) else "aquario"
elif mes == 2:
    signo_zodiacal = "aquario" if (dia < 19) else "picis"
elif mes == 3:
    signo_zodiacal = "picis" if (dia < 21) else "aries"
elif mes == 4:
    signo_zodiacal = "aries" if (dia < 20) else "tauro"
elif mes == 5:
    signo_zodiacal = "tauro" if (dia < 21) else "geminis"
elif mes == 6:
    signo_zodiacal = "gemini" if (dia < 21) else "cancer"
elif mes == 7:
    signo_zodiacal = "cancer" if (dia < 23) else "leo"
elif mes == 8:
    signo_zodiacal = "leo" if (dia < 23) else"'virgo"
elif mes == 9:
    signo_zodiacal = "virgo" if (dia < 23) else "libra"
elif mes == 10:
    signo_zodiacal = "libra" if (dia < 23) else "escorpio"
elif mes == 11:
    signo_zodiacal = "escorpio" if (dia < 22) else "sagitario"
print(signo_zodiacal)
