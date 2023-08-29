#Zodiaco
signo = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
fecha = [22, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 23]

dia = int(input("Dia de nacimiento: "))
mes = int(input("Mes de nacimiento: "))

mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print("Su signo zodiacal es ", signo[mes])      