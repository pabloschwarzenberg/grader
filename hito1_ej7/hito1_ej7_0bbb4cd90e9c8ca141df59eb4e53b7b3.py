#Zodiaco
signo = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Gémenis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
fecha = [20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22]


dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))

mes -= 1

if dia > fecha[mes]:
    mes += 1
if mes == 12:
    mes = 0

print ("El signo zodiacal es: " + signo[mes])