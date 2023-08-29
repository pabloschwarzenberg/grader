#Zodiaco
signo = ["aries", "tauro", "geminis", "cancer", "leon", "virgo", "libra", "escorpion", "sagitario", "capricornio", "acuario", "piscis"]
fecha = [20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21]
print("Hola estudiante")

mes = int(input("Ingrese su mes de nacimiento: "))
dia = int(input("Ingrese su dia de nacimiento: "))

mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0
print ("Su signo zodiacal es", signo[mes])
     