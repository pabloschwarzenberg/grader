#Zodiaco
sign = ("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario")
dates = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

day = int(input("Día :"))
month = int(input("Mes :"))

month = month - 1
if day > dates[month]:
    month = month + 1
if month == 12:
    month = 0

print ("Tu signo es: " + sign[month])