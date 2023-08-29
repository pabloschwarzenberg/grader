#Zodiaco
signo = ["capricornio", "acuario", "piscis", "aries", "tauro", "geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario"] 
fecha = [20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21]

mes = int(input("mes de nacimiento: "))
dia = int(input("dia de nacimiento: "))

mes = mes - 1
if dia > fecha[mes]:
  mes = mes + 1
if mes == 12:
  mes = 0

print("su signo zodical es ", signo[mes])