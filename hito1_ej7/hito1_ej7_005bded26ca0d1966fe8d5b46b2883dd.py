#Zodiaco

signo = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Libra", "Virgo", "Libra", "Escorpio", "Sagitario"]
fecha = [22, 19, 21, 20, 21, 21, 20, 23, 23, 23, 23, 22]

dia = int(input("Ingrese su dia: "))
mes = int(input("Ingrese su mes: "))

if dia < fecha[mes]:
    mes -= 1
else:
    mes += 1
if mes == 12:
    mes = 0

print("su signo zodiacal es: ", signo[mes])      