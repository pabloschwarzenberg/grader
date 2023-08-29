#Zodiaco
signo = ("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

dia=int(input("Ingrese dia de nacimiento: "))
mes=int(input(" Ingrese mes de nacimiento en numeros :"))

mes=mes-1
if dia>fechas[mes]:
    mes=mes+1
if mes==12:
    mes=0

print ("Tu signo es: " + signo[mes])