#Zodiaco
s = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
f = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

d=int(input("Ingrese dia de nacimiento:"))
m=int(input(" Ingrese mes de nacimiento :"))

m=m-1
if d>f[m]:
    m=m+1
if m==12:
    m=0

print ("Tu signo es: " + s[m])