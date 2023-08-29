#Zodiaco
print("Signo del zodiaco")
zigno = ["capricornio","Acuario","piscis","tauro","gemesis","cancer","leo","virgo","libra","tauro","sagitario" ]
fecha = [20,19,20,21,21,22,22,22,22,22,21,]

mes = int(input("mes de nacimiento: "))
dia  = int(input("Dia de naciemnto: "))

mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
if mes ==12 :
    mes = 0

print("Su signo zodiacal es" , zigno[mes])      