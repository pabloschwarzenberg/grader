#Zodiaco
signo = ["capricornio", "acuario", "piscis", "aries", "tauro", "geminis", "cancer", "leo", "virgo", "libra", "escorpion", "sagitarios" ]
fecha = [20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21]


 # datos del usuario
dia = int(input("dia de nacimineto: ")) 
mes = int(input("mes de nacimineto: "))

mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print ("su signo zodiaca es ", signo[mes])      