#Zodiaco
Signo=["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"]
Fecha=[22,19,18,20,21,21,22,22,22,22,21]
Dia=int(input("Indique su dia de nacimiento:"))
Mes=int(input("Indique su mes de nacimiento:"))

Mes=Mes-1
if Dia > Fecha[Mes]:
    Mes=Mes+1
if Mes == 12:
    Mes = 0
print("Su signo Zodiacal es",Signo[Mes])     