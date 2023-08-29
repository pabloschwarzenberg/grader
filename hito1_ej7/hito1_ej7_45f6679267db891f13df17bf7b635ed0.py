#Zodiaco
print("calcularemos tu signo del zodiaco")
signoszodiaco = ("capricornio", "acuario", "piscis", "aries", "tauro", " geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechasignos = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

x=int(input("dia :"))
y=int(input("mes :"))

y=y-1
if x>fechasignos[y]:
    y=y+1
if y==12:
    y=0

print("tu signo corresponde a: "+ signoszodiaco[y])      