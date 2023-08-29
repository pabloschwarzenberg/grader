# Zodiaco
x = ("Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio",
     "Sagitario")
y = (20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22)

Dia = int(input("Ingrese Día de nacimiento: "))
Mes = int(input("Ingrese Mes de nacimiento en número: "))

Mes = Mes-1
if Dia>y[Mes]:
   Mes = Mes + 1
if Mes==12:
   Mes=0

print(x[Mes])