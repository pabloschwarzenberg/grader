#Zodiaco
signoszodiacales = ["Capricornio","Acuario", "Piscis", "Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"]
fechas = [20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22]
print("Escriba el día en que nació: ")
dia=int(input())
print("Escriba el mes en que nació: ")
mes=int(input())
mes=mes-1
if dia > fechas[mes]:
    mes=mes+1
if mes==12:
    mes=0
print("Su signo sodiacal es: ", signoszodiacales[mes])        