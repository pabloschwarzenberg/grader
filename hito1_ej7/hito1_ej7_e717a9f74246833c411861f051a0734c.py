#Zodiaco
signo=["capricornio","acuario","piscis","aries","tauro","gemenis","cáncer","leo","virgo","libra","escorpio","sagitario"]
fecha=[19,16,12,19,14,20,21,10,16,31,23,30,18]
dia= int(input("dia de nacimiento:"))
mes =int(input("mes de nacimiento:"))
if dia > fecha[mes]:
    mes = mes+1
if mes ==12:
    mes=0   
print (signo[mes-1])