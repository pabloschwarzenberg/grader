#Zodiaco
signos=["Capricornio","Acuario","Piscis","Aries","Tauro","Géminis","Cáncer","Leo","Virgo","Libra","Escorpio","Sagitario"]
fechas=[19,18,20,19,20,20,22,22,22,22,21,21]
dia=int(input("Ingrese el dia en que nacio: "))
mes=int(input("Ingrese el mes en el que nacio: "))
if dia>fechas[mes]:
  mes=mes+1
if mes==12:
  mes=0
print("Su Signo Zodiacal es",signos[mes-1])      