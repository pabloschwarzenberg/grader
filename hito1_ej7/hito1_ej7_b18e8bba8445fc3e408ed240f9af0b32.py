#Zodiaco
signo =["capricornio","acuario", "piscis", "aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario"]
fecha =[20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22]
dia =int(input("Escriba el día que nació:"))
mes =int(input("Escriba el mes que nació:"))
mes=mes -1
if dia>fecha[mes]:
    mes = mes + 1
if mes==12:
    mes= 0
print("Su signo sodiacal es: ",signo[mes])     