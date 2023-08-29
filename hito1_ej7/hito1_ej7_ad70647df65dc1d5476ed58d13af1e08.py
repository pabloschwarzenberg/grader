#Zodiaco
dia = int(input("Ingresa el día de tu cumpleaños (1-31): "))
mes = int(input("Ingresa el mes de tu cumpleaños (1-12): "))

signo_zodiaco = ""
if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo_zodiaco = "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo_zodiaco = "Piscis"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo_zodiaco = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo_zodiaco = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo_zodiaco = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo_zodiaco = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo_zodiaco = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo_zodiaco = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo_zodiaco = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo_zodiaco = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo_zodiaco = "Sagitario"
else:
    signo_zodiaco = "Capricornio"

print("Tu signo del zodíaco es:", signo_zodiaco)
      