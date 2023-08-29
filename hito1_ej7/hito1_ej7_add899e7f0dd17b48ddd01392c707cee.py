#Zodiaco
signo=("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario")
fechas=(20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

dia=int(input("Ingresa el día: "))
mes=int(input("Ingresa el mes: "))

mes=mes-1
if dia>fechas[mes]:
    mes=mes+1
if mes==12:
    mes=0

print("Tu signo es: "+signo[mes])