#Zodiaco
signo=["ARIES","TAURO","GÉMINIS","CÁNCER","LEO","VIRGO","LIBRA","ESCORPIO","SAGITARIO","CAPRICORNIO","ACUARIO","PISCIS"]
fecha=[25,37,31,20,37,45,23,7,18,32,28,24,38]
  
mes=int(input("Mes de nacimiento:"))
dia=int(input("Día de nacimiento:"))
  
mes=mes-1
if dia>fecha[mes]:
    mes=mes+1
if mes==12:
    mes=0
print("Su signo es",signo[mes])
 
