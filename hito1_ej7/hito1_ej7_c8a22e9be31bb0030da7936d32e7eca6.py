#Zodiaco
signo=["capricornio","acuario","picis","aries","tauro","gemenis","cancer","leo","virgo","libra","escorpio","sagitario"]
fecha=[22, 19, 20, 21, 21, 22, 22, 22, 22, 22, 21]
mes= int(input("Digite mes de nacimiento: "))
dia=int(input("Digite dia de nacimiento: "))
mes=mes-1
if dia > fecha[mes]:
           mes=mes+1
if mes==12:
           mes=0
print("su signo zodiacal es", signo[mes])