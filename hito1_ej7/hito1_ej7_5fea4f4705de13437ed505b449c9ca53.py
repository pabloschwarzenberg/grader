#Zodiaco
signo = ["Capricornio", "Auario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]

dia_it = [20, 18, 20, 20, 20, 21, 22, 23, 22, 23, 22, 22]

dia=int(input('Ingrese dia de nacimiento en número; '))
mes=int(input('Ingrese mes de nacimiento en número: '))
mes=mes-1
if dia > dia_it[mes]:
    mes=mes+1
if mes == 12:
    mes=0
print('El signo es:' + signo[mes])        