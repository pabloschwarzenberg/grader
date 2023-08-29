#Zodiaco
signo = ("capricornio","acuario","piscis","aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

dia=int(input("Dia :"))
mes=int(input("Mes :"))

mes=mes-1
if dia>fechas[mes]:
    mes=mes+1
elif mes==12:
    mes=0

print(signo[mes])      