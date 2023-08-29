#Zodiaco
signos = ["capricornio","acuario","piscis","aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario"]
fechas= [19,18,20,19,20,20,22,22,22,22,21,21]
dia=int (input("digite su dia de cumpleaños como numero: "))
mes=int(input("digite su mes de nacimiento como numero: "))
if dia>fechas[mes]:
  mes= mes+1
if mes== 12:
  mes=0
print(signos[mes-1])