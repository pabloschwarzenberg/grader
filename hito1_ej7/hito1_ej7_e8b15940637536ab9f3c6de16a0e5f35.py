#Zodiaco
signo = ['capricornio','acuario','piscis','aries','tauro','geminis','cancer','leo','virgo','libra','escorpio','sagitario']
fecha = [20,19,20,21,21,22,22,22,22,22,21]
dia = int(input('Ingresa tu dia de nacimiento:'))
mes = int(input('Ingresa tu mes de nacimiento:'))


mes = mes - 1 
if dia > fecha[mes]:
  mes = mes + 1
if mes == 12:
  mes = 0
print ('Su signo zodiacal es:',signo[mes])