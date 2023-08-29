#Zodiaco
signos = ["capricornio","acuario","piscis","aries","tauro","geminis","cancer","leo","virgo","libra","escorpion","sagitario"]      
fechas = [19,18,20,19,20,20,22,22,22,22,21,21]
dia = int(input("Digite su dia de cumpleaños como numeros: "))
mes = int(input("Digite su mes de nacimiento como numeros: "))

if dia > fechas[mes]:
    mes = mes+1
if mes == 12:
    mes = 0
    
print(signos[mes-1])