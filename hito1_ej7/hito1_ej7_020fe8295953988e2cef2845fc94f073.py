#Zodiaco
# Pedir al usuario que ingrese el día y el mes de cumpleaños
dia = int(input("Ingrese el día de cumpleaños (1-31): "))
mes = int(input("Ingrese el mes de cumpleaños (1-12): "))

# Determinar el signo del zodíaco
if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 19):
    signo = "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 21):
    signo = "Piscis"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 21):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 23):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
    signo = "Escorpio"
elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 22):
    signo = "Sagitario"
else:
    signo = "Capricornio"

# Imprimir el signo del zodíaco
print("El signo del zodíaco es:", signo)