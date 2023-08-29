#Zodiaco
signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
a=int(input("dia :"))
b=int(input("mes :"))
b=b-1
if a>fechas[b]:
    b=b+1
if a<fechas[b]:
    b=b
if b==12:
    b=0
print (signo[b])