#Zodiaco
signo= ["Capricornio","Acuario","Pisces","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"]
dias = [20,19,21,20,21,21,23,23,23,23,22,22]
dia= int(input("Ingrese el dia en que nacio : "),)
mes= int(input("Ingrese el mes en que nacio : "),)
mes = mes - 1
if dia >= dias[mes]:
  mes = mes + 1
if mes == 12:
  mes = 0
print("Su signo zodiacal es: ",signo[mes])
