#Zodiaco
## ENTRADA DATOS - PROCESO -SALIDA

Dia = int(input("Ingresa el día de tu Cumpleaños (1-31): "))
Mes = int(input("Ingresa el mes de Cumpleaños (1-12) : "))

Signo = ""

if (Mes == 1 and Dia >= 20) or (Mes == 2 and Dia <= 18):
    Signo = "ACUARIO"
elif (Mes == 2 and Dia >= 19) or (Mes == 3 and Dia <= 20):
    Signo = "PISCIS" 
elif (Mes == 3 and Dia >= 21) or (Mes == 4 and Dia <= 19):
    Signo = "ARIES"
elif (Mes == 4 and Dia >= 20) or (Mes == 5 and Dia <= 20):
    Signo = "TAURO"
elif (Mes == 5 and Dia >= 21) or (Mes == 6 and Dia <= 20):
    Signo = "GEMINIS"
elif (Mes == 6 and Dia >= 21) or (Mes == 7 and Dia <= 22):
    Signo = "CÁNCER"
elif (Mes == 7 and Dia >= 23) or (Mes == 8 and Dia <= 22):
    Signo = "LEO"
elif (Mes == 8 and Dia >= 23) or (Mes == 9 and Dia <= 22):
    Signo = "VIRGO"
elif (Mes == 9 and Dia >= 23) or (Mes == 10 and Dia <= 22):
    Signo = "LIBRA"
elif (Mes == 10 and Dia >= 23) or (Mes == 11 and Dia <= 21):
    Signo = "ESCORPION"
elif (Mes == 11 and Dia >= 22) or (Mes == 12 and Dia <= 21):
    Signo = "SAGITARIO"
elif (Mes == 12 and Dia >= 22) or (Mes == 1 and Dia <= 19):
    Signo = "CAPRICORNIO"
else:
    Signo = "Fecha de Cumpleaños Invalida"

print("Tu Signo del Zodíaco es: ", Signo)   