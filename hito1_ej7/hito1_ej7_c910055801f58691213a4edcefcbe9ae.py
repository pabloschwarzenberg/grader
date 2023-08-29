#Zodiaco
day = int(input("Día de nacimiento >>> "))
month = int(input("Mes de nacimiento >>> "))
if month == 3 and 22 <= day <= 31 or month == 4 and 1 <= day <= 20:
    sign = "Aries"
elif month == 4 and 21 <= day <= 30 or month == 5 and 1 <= day <= 21:
    sign = "Tauro"
elif month == 5 and 22 <= day <= 31 or month == 6 and 1 <= day <= 21:
    sign = "Géminis"
elif month == 6 and 22 <= day <= 30 or month == 7 and 1 <= day <= 23:
    sign = "Cáncer"
elif month == 7 and 24 <= day <= 31 or month == 8 and 1 <= day <= 23:
    sign = "Leo"
elif month == 8 and 24 <= day <= 31 or month == 9 and 1 <= day <= 23:
    sign = "Virgo"
elif month == 9 and 24 <= day <= 30 or month == 10 and 1 <= day <= 23:
    sign = "Libra"
elif month == 10 and 24 <= day <= 31 or month == 11 and 1 <= day <= 22:
    sign = "Escorpio"
elif month == 11 and 23 <= day <= 30 or month == 12 and 1 <= day <= 22:
    sign = "Sagitario"
elif month == 12 and 23 <= day <= 31 or month == 1 and 1 <= day <= 20:
    sign = "Capricornio"
elif month == 1 and 21 <= day <= 31 or month == 2 and 1 <= day <= 19:
    sign = "Acuario"
elif month == 2 and 20 <= day <= 28 or month == 3 and 1 <= day <= 21:
    sign = "Piscis"
else:
  print("fecha inválida")
print(sign)