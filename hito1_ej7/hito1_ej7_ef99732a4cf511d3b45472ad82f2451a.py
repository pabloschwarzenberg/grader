D = int(input("Ingresa el día de tu cumpleaños: "))
M = int(input("Ingresa el mes de tu cumpleaños: "))

if (M == 1 and D >= 20) or (M == 2 and D <= 19):
    Zodiac = "Acuario"
elif (M == 2 and D >= 19) or (M == 3 and D <= 21):
    Zodiac = "Piscis"
elif (M == 3 and D >= 21) or (M == 4 and D <= 20):
    Zodiac = "Aries"
elif (M == 4 and D >= 20) or (M == 5 and D <= 21):
    Zodiac = "Tauro"
elif (M == 5 and D >= 21) or (M == 6 and D <= 21):
    Zodiac = "Geminis"
elif (M == 6 and D >= 21) or (M == 7 and D <= 23):
    Zodiac = "Cancer"
elif (M == 7 and D >= 23) or (M == 8 and D <= 23):
    Zodiac = "Leo"
elif (M == 8 and D >= 23) or (M == 9 and D <= 23):
    Zodiac = "Virgo"
elif (M == 9 and D >= 23) or (M == 10 and D <= 23):
    Zodiac = "Libra"
elif (M == 10 and D >= 23) or (M == 11 and D <= 23):
    Zodiac = "Escorpio"
elif (M == 11 and D >= 23) or (M == 12 and D <= 22):
    Zodiac = "Sagitario"
elif (M == 12 and D >= 22) or (M == 1 and D <= 20):
    Zodiac = "Capricornio"
else:
    Zodiac = "Fecha inválida"


print("Tu signo es:", Zodiac)