#Zodiaco
dia_cumple = int(input("Ingrese el día de su cumpleaños: "))
mes_cumple = int(input("Ingrese el mes de su cumpleaños: "))

signo_zodiacal = ""

if (mes_cumple == 1 and 20 <= dia_cumple <= 31) or (mes_cumple == 2 and 1 <= dia_cumple <= 18):
    signo_zodiacal = "Acuario"
elif (mes_cumple == 2 and 19 <= dia_cumple <= 29) or (mes_cumple == 3 and 1 <= dia_cumple <= 20):
    signo_zodiacal = "Piscis"
elif (mes_cumple == 3 and 21 <= dia_cumple <= 31) or (mes_cumple == 4 and 1 <= dia_cumple <= 19):
    signo_zodiacal = "Aries"
elif (mes_cumple == 4 and 20 <= dia_cumple <= 30) or (mes_cumple == 5 and 1 <= dia_cumple <= 20):
    signo_zodiacal = "Tauro"
elif (mes_cumple == 5 and 21 <= dia_cumple <= 31) or (mes_cumple == 6 and 1 <= dia_cumple <= 20):
    signo_zodiacal = "Géminis"
elif (mes_cumple == 6 and 21 <= dia_cumple <= 30) or (mes_cumple == 7 and 1 <= dia_cumple <= 22):
    signo_zodiacal = "Cáncer"
elif (mes_cumple == 7 and 23 <= dia_cumple <= 31) or (mes_cumple == 8 and 1 <= dia_cumple <= 22):
    signo_zodiacal = "Leo"
elif (mes_cumple == 8 and 23 <= dia_cumple <= 31) or (mes_cumple == 9 and 1 <= dia_cumple <= 22):
    signo_zodiacal = "Virgo"
elif (mes_cumple == 9 and 23 <= dia_cumple <= 30) or (mes_cumple == 10 and 1 <= dia_cumple <= 22):
    signo_zodiacal = "Libra"
elif (mes_cumple == 10 and 23 <= dia_cumple <= 31) or (mes_cumple == 11 and 1 <= dia_cumple <= 21):
    signo_zodiacal = "Escorpio"
elif (mes_cumple == 11 and 22 <= dia_cumple <= 30) or (mes_cumple == 12 and 1 <= dia_cumple <= 21):
    signo_zodiacal = "Sagitario"
elif (mes_cumple == 12 and 22 <= dia_cumple <= 31) or (mes_cumple == 1 and 1 <= dia_cumple <= 19):
    signo_zodiacal = "Capricornio"
else:
    signo_zodiacal = "Fecha de cumpleaños inválida"

print("Su signo zodiacal es:", signo_zodiacal)
      