#Zodiaco
signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

dia=int(input("ingrese su dia de nacimiento :"))
mes=int(input("ingrese su mes de nacimiento :"))

mes=mes-1
if dia>fechas[mes]:
    mes=mes+1
if mes==12:
    mes=0

print ("Tu signo es: " + signo[mes])