#Zodiaco
Zodiaco = ("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Libra", "Virgo", "Libra", "Escorpio", "Sagitario")
Fechas = [22, 19, 21, 20, 21, 21, 20, 23, 23, 23, 23, 22]


Dia = int(input("ingrese el dia de cumpleaños: "))
Mes = int(input("ingrese el mes de cumpleaños: "))

Mes = Mes - 1

if Dia > Fechas[Mes]:
  Mes = Mes + 1
  
if Mes == 12:
  Mes = 0

#Fin
print("su signo es: ", Zodiaco[Mes])
