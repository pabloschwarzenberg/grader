#Zodiaco
      # Obtener el día y el mes de cumpleaños del usuario
dia = int(input("Ingrese el día de su cumpleaños (1-31): "))
mes = int(input("Ingrese el mes de su cumpleaños (1-12): "))

# Determinar el signo del zodíaco
if (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 19):
    signo = "Aries"
elif (mes == 4 and 20 <= dia <= 30) or (mes == 5 and 1 <= dia <= 20):
    signo = "Tauro"
elif (mes == 5 and 21 <= dia <= 31) or (mes == 6 and 1 <= dia <= 20):
    signo = "Géminis"
elif (mes == 6 and 21 <= dia <= 30) or (mes == 7 and 1 <= dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and 23 <= dia <= 31) or (mes == 8 and 1 <= dia <= 22):
    signo = "Leo"
elif (mes == 8 and 23 <= dia <= 31) or (mes == 9 and 1 <= dia <= 22):
    signo = "Virgo"
elif (mes == 9 and 23 <= dia <= 30) or (mes == 10 and 1 <= dia <= 22):
    signo = "Libra"
elif (mes == 10 and 23 <= dia <= 31) or (mes == 11 and 1 <= dia <= 21):
    signo = "Escorpio"
elif (mes == 11 and 22 <= dia <= 30) or (mes == 12 and 1 <= dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and 22 <= dia <= 31) or (mes == 1 and 1 <= dia <= 19):
    signo = "Capricornio"
elif (mes == 1 and 20 <= dia <= 31) or (mes == 2 and 1 <= dia <= 18):
    signo = "Acuario"
elif (mes == 2 and 19 <= dia <= 29) or (mes == 3 and 1 <= dia <= 20):
    signo = "Piscis"
else:
    signo = "Fecha de cumpleaños inválida"

# Imprimir el signo del zodíaco
print("Su signo del zodíaco es:", signo)
