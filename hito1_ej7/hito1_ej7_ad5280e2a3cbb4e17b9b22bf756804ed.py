#Zodiaco

dia_cumple = int(input("Ingresa el día de tu cumpleaños (1-31): "))
mes_cumple = int(input("Ingresa el mes de tu cumpleaños (1-12): "))


if (mes_cumple == 1 and dia_cumple >= 20) or (mes_cumple == 2 and dia_cumple <= 18):
    signo = "Acuario"
elif (mes_cumple == 2 and dia_cumple >= 19) or (mes_cumple == 3 and dia_cumple <= 20):
    signo = "Piscis"
elif (mes_cumple == 3 and dia_cumple >= 21) or (mes_cumple == 4 and dia_cumple <= 19):
    signo = "Aries"
elif (mes_cumple == 4 and dia_cumple >= 20) or (mes_cumple == 5 and dia_cumple <= 20):
    signo = "Tauro"
elif (mes_cumple == 5 and dia_cumple >= 21) or (mes_cumple == 6 and dia_cumple <= 20):
    signo = "Géminis"
elif (mes_cumple == 6 and dia_cumple >= 21) or (mes_cumple == 7 and dia_cumple <= 22):
    signo = "Cáncer"
elif (mes_cumple == 7 and dia_cumple >= 23) or (mes_cumple == 8 and dia_cumple <= 22):
    signo = "Leo"
elif (mes_cumple == 8 and dia_cumple >= 23) or (mes_cumple == 9 and dia_cumple <= 22):
    signo = "Virgo"
elif (mes_cumple == 9 and dia_cumple >= 23) or (mes_cumple == 10 and dia_cumple <= 22):
    signo = "Libra"
elif (mes_cumple == 10 and dia_cumple >= 23) or (mes_cumple == 11 and dia_cumple <= 21):
    signo = "Escorpio"
elif (mes_cumple == 11 and dia_cumple >= 22) or (mes_cumple == 12 and dia_cumple <= 21):
    signo = "Sagitario"
else:
    signo = "Capricornio"


print("Tu signo del zodíaco es: ", signo)
