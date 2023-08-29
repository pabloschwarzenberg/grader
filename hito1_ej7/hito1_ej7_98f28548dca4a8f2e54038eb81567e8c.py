#Zodiaco
signo = ("Capricornio","Acuario","Piscis","Aries","Tauro","Géminis","Cancer","Leo","Virgo","Libra","Escrpion","Sagitario")
fechas = (20,19,21,20,21,21,23,23,23,23,22,20)

dia=int(input("dia: "))
mes=int(input("mes: "))

mes = mes - 1
if dia > fechas[mes]:
    mes += 1
if mes == 12:
    mes = 0

print(signo[mes])