#Zodiaco
dia=int(input("Por favor ingrese el dia que está de cumpleaños: "))
mes=int(input("Por favor ingrese el mes que está de cumpleaños numericamente (ej: si es mayo, ingrese 5): "))

# Determinar el signo de zodiaco a partir de las fechas y meses
# Van numeradas las fechas por el zodiaco tropical

# aries: 21 marzo - 20 abril
if ((mes==3 and dia>=21) or (mes==4 and dia <=20)):
	print("Tu signo zodiacal es aries")
# tauro: 21 abril - 20 mayo
elif ((mes==4 and dia>=21) or (mes==5 and dia <=20)):
	print("Tu signo zodiacal es tauro")
# gemini: 21 mayo - 20 junio
elif ((mes==5 and dia>=21) or (mes==6 and dia <=20)):
	print("Tu signo zodiacal es gemini")
# cancer: 21 junio - 21 julio
elif ((mes==6 and dia>=21) or (mes==7 and dia <=21)):
	print("Tu signo zodiacal es cancer")
# leo: 22 julio - 22 agosto
elif ((mes==7 and dia>=22) or (mes==8 and dia <=22)):
	print("Tu signo zodiacal es leo")
# virgo: 23 agosto - 22 septiembre
elif ((mes==8 and dia>=23) or (mes==9 and dia <=22)):
	print("Tu signo zodiacal es virgo")
# libra: 23 septiembre - 22 octubre
elif ((mes==9 and dia>=23) or (mes==10 and dia <=22)):
	print("Tu signo zodiacal es libra")
# escorpio: 23 octubre - 21 noviembre
elif ((mes==10 and dia>=23) or (mes==11 and dia <=21)):
	print("Tu signo zodiacal es escorpio")
# sagitario: 22 noviembre - 21 diciembre
elif ((mes==11 and dia>=22) or (mes==12 and dia <=21)):
	print("Tu signo zodiacal es sagitario")
# capricornio: 22 diciembre - 19 enero
elif ((mes==12 and dia>=22) or (mes==1 and dia <=19)):
	print("Tu signo zodiacal es capricornio")
# acuario: 20 enero - 18 febrero
elif ((mes==1 and dia>=20) or (mes==2 and dia <=18)):
	print("Tu signo zodiacal es acuario")
# piscis: 19 febrero - 21 marzo
elif ((mes==2 and dia>=19) or (mes==2 and dia <=21)):
	print("Tu signo zodiacal es piscis")