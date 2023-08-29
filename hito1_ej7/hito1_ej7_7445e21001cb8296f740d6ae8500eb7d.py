#zodiaco
signo = ["capricornio", "acuario", "piscis", "aries", "tauro", "geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario"]
fecha = [20,19,20,21,21,22,22,22,22,22,21,23,22]

dia = int(input("ingrese su dia de nacimiento "))
mes = int(input("ingrese su mes de nacimiento "))

mes = mes - 1
if mes == 12:
  mes = 0
if dia > fecha[mes]:
  mes += 1

print("su signo zodiacal es ", signo[mes])