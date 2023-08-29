#Zodiaco
signo = ["Capricornio", "Acuario", "Picis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
fecha = [22, 20, 19, 21, 20, 21, 21, 22, 22, 22, 22, 22]

dia = int(input("Ingrese dia de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento: "))


mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1

if mes == 12:
    mes = 0

print(signo[mes])     