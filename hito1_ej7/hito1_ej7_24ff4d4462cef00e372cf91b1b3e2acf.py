signo=("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario")
f= (20, 19, 20, 21, 21, 22, 22, 22, 22, 22, 22, 21)
d= int(input("Ingrese su Día de Nacimiento: "))
m= int(input("Ingrese el número de Mes de su Nacimiento: "))
m= m-1
if d>f[m]:
    m=m+1
if m==12:
    m=0

print("Su signo Zodiacal es: " + signo[m])

      