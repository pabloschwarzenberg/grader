#Zodiaco
signo=["capricornio","acuario","picis","aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario"]
fecha=[20,19,20,20,21,21,22,22,22,22,22,21]

dia=int(input("dia de nacimiento"))
mes=int(input("mes de nacimiento"))

mes=mes-1
if dia >fecha[mes]:
    mes=mes+1
if mes==12:
    mes=0

print(signo[mes])