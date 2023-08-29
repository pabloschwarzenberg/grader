#Zodiaco
signos = ["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Càncer","Leo","Virgo","Libra","Escorpio","Sagitario"]
fechas = [19,18,20,19,20,20,22,22,22,22,21,21]
dia = int(input("Digite su dia de cumpleaños como número:"))
mes = int(input("Digite su mes de nacimiento como número:"))
if dia > fechas[mes]:
   mes = mes + 1
if mes == 12:
   mes = 0
print(signos[mes-1])   