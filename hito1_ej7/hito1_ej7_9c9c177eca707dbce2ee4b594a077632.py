#Zodiaco
# Solicitar al usuario el día y el mes de cumpleaños
dia = int(input("Ingrese el día de su cumpleaños: "))
mes = int(input("Ingrese el mes de su cumpleaños: "))

# Determinar el signo del zodíaco
signo = ""

if (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 20):
    signo = "Aries"
elif (mes == 4 and 21 <= dia <= 30) or (mes == 5 and 1 <= dia <= 21):
    signo = "Tauro"
elif (mes == 5 and 22 <= dia <= 31) or (mes == 6 and 1 <= dia <= 21):
    signo = "Géminis"
elif (mes == 6 and 22 <= dia <= 30) or (mes == 7 and 1 <= dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and 23 <= dia <= 31) or (mes == 8 and 1 <= dia <= 23):
    signo = "Leo"
elif (mes == 8 and 24 <= dia <= 31) or (mes == 9 and 1 <= dia <= 23):
    signo = "Virgo"
elif (mes == 9 and 24 <= dia <= 30) or (mes == 10 and 1 <= dia <= 23):
    signo = "Libra"
elif (mes == 10 and 24 <= dia <= 31) or (mes == 11 and 1 <= dia <= 22):
    signo = "Escorpio"
elif (mes == 11 and 23 <= dia <= 30) or (mes == 12 and 1 <= dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and 22 <= dia <= 31) or (mes == 1 and 1 <= dia <= 20):
    signo = "Capricornio"
elif (mes == 1 and 21 <= dia <= 31) or (mes == 2 and 1 <= dia <= 19):
    signo = "Acuario"
elif (mes == 2 and 20 <= dia <= 29) or (mes == 3 and 1 <= dia <= 20):
    signo = "Piscis"

# Imprimir el signo del zodíaco
print("Signo del zodíaco:", signo)
