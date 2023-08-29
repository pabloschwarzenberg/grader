#Zodiaco
signo = ["Capricornio", "Acuario", "Pisics", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "libra", "Escorpio", "Sagitario"]
fecha = [20, 19, 20, 21, 21, 22, 22, 22, 22, 22, 21]


dia = int(input("dia de nacimiento: "))
mes = int(input("mes de Nacimiento: "))


mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print ("Su signo Zodiacal es ", signo [mes])
      