#Zodiaco
signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

d = int(input("dia: "))
m = int(input("mes: "))

m = m-1
if d > fechas[m]:
    m += 1
if m == 12:
    m = 0

print("El signo es: " + signo[m])