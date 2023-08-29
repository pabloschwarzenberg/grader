#Zodiaco
signo = ("aries", "tauro", "geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario", "capricornio", "acuario", "piscis")
fechas = (21,20,21,21,23,23,23,23,23,22,20,19)
dia= int(input("dia :"))
mes= int(input("mes :"))
mes= mes-1
if dia>fechas[mes]:
  mes=mes+1
if mes==12:
  mes = 0
print (signo[mes])