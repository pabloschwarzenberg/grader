#Zodiaco
Signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
Fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

Dia=int(input("Dia :"))
Mes=int(input("Mes :"))

Mes=Mes-1
if Dia>Fechas[Mes]:
    Mes=Mes+1
if Mes==12:
    Mes=0

print ("Tu signo es: " + Signo[Mes])     