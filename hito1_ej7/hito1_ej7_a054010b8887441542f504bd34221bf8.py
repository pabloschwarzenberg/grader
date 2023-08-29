#Zodiaco
d=int(input("ingrese el dia de tu cumpleaños :"))
date=int(input("ingrese el mes de tu cumpleaños :"))

sig = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
date2 = (20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22)

date=date-1
if d>date2[date]:
    date=date+1
if date==12:
    date=0

print ("Tu signo sodiacal es= " + sig[date])
     