#Zodiaco
Signo_zodiacal = ("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "sagitario")
fechas = (20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22)

dia=int(input("dia: "))
mes=int(input("mes: "))

mes= mes-1
if dia>fechas[mes]:
    mes= mes+1
if mes == 12:
    mes = 0

print ("Tu signo es: " + Signo_zodiacal[mes])