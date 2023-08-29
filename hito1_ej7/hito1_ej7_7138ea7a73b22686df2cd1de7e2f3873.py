signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

d = int(input("Introduzca su día de cumpleaños: "))
m = int(input("Introduzca su mes de cumpleaños: "))

m = m - 1
if d > fechas [m]:
    m = m + 1
if m == 12:
    m = 0

print("Su signo zodiacal es:  " + signo[m])