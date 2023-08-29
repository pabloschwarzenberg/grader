#Zodiaco
Signos = ("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpion", "Sagitario")
Fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

Dia = int(input("Ingrese el dia de su nacimiento: "))
Mes = int(input("Ingrese el mes de su nacimiento: "))

Mes = Mes - 1
if Dia > Fechas [Mes]:
  Mes = Mes + 1
if Mes ==12:
  Mes = 0
print ("Su signo del zodiaco es:  " + Signos [Mes])