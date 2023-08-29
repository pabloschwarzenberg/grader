#Zodiaco
# Solicitar al usuario el día y el mes de cumpleaños
dia_cumple = int(input("Ingrese el día de su cumpleaños: "))
mes_cumple = int(input("Ingrese el mes de su cumpleaños: "))

# Determinar el signo del zodíaco
signo_zodiaco = ""

if (mes_cumple == 1 and dia_cumple >= 20) or (mes_cumple == 2 and dia_cumple <= 18):
    signo_zodiaco = "Acuario"
elif (mes_cumple == 2 and dia_cumple >= 19) or (mes_cumple == 3 and dia_cumple <= 20):
    signo_zodiaco = "Piscis"
elif (mes_cumple == 3 and dia_cumple >= 21) or (mes_cumple == 4 and dia_cumple <= 19):
    signo_zodiaco = "Aries"
elif (mes_cumple == 4 and dia_cumple >= 20) or (mes_cumple == 5 and dia_cumple <= 20):
    signo_zodiaco = "Tauro"
elif (mes_cumple == 5 and dia_cumple >= 21) or (mes_cumple == 6 and dia_cumple <= 20):
    signo_zodiaco = "Géminis"
elif (mes_cumple == 6 and dia_cumple >= 21) or (mes_cumple == 7 and dia_cumple <= 22):
    signo_zodiaco = "Cáncer"
elif (mes_cumple == 7 and dia_cumple >= 23) or (mes_cumple == 8 and dia_cumple <= 22):
    signo_zodiaco = "Leo"
elif (mes_cumple == 8 and dia_cumple >= 23) or (mes_cumple == 9 and dia_cumple <= 22):
    signo_zodiaco = "Virgo"
elif (mes_cumple == 9 and dia_cumple >= 23) or (mes_cumple == 10 and dia_cumple <= 22):
    signo_zodiaco = "Libra"
elif (mes_cumple == 10 and dia_cumple >= 23) or (mes_cumple == 11 and dia_cumple <= 21):
    signo_zodiaco = "Escorpio"
elif (mes_cumple == 11 and dia_cumple >= 22) or (mes_cumple == 12 and dia_cumple <= 21):
    signo_zodiaco = "Sagitario"
elif (mes_cumple == 12 and dia_cumple >= 22) or (mes_cumple == 1 and dia_cumple <= 19):
    signo_zodiaco = "Capricornio"

# Imprimir el resultado
print("Signo del zodíaco:", signo_zodiaco)      