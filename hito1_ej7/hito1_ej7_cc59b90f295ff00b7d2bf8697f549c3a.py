#Zodiaco
      
signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

d=int(input("ingresar el dia de tu compleaños(1 al 31):"))
m=int(input("ingresa el mes de tu cumpleaños(1 al 12):"))

m=m-1
if d>fechas[m]:
    m=m+1
if m==12:
    m=0

print ("Tu signo es: " + signo[m])
