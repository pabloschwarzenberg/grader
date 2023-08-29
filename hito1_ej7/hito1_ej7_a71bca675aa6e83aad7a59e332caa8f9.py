#Zodiaco
 dia = int(input("Ingrese el día de su cumpleaños (1-31): "))
mes = int(input("Ingrese el mes de su cumpleaños (1-12): "))

if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "piscis"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "geminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = 'virgo'
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "sagitario"
else:
    signo = "capricornio"

print("Tu signo del zodíaco es:", signo)     