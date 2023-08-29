#Zodiaco
d = int(input("Indique su día de cumpleaños: "))
m = int(input("Indique su mes de cumpleaños: "))

if m == 3 and d >= 21 and d <= 31 or m == 4 and d <= 20:
    print("Aries")
if m == 4 and d >= 20 and d <= 30 or m == 5 and d <= 21:
    print("Taurus")
if m == 5 and d >= 21 and d <= 31 or m == 6 and d <= 21:
    print("Geminis")
if m == 6 and d >= 21 and d <= 30 or m == 7 and d <= 23:
    print("Cáncer")
if m == 7 and d >= 23 and d <= 31 or m == 8 and d <= 23:
    print("Leo")
if m == 8 and d >= 23 and d <= 31 or m == 9 and d <= 23:
    print("Virgo")
if m == 9 and d >= 23 and d <= 30 or m == 10 and d <= 23:
    print("Libra")
if m == 10 and d >= 23 and d <= 31 or m == 11 and d <= 22:
    print("Escorpio")
if m == 11 and d >= 23 and d <= 30 or m == 12 and d <= 22:
    print("Sagitario")
if m == 12 and d >= 22 and d <= 31 or m == 1 and d <= 20:
    print("Capricornio")
if m == 1 and d >= 20 and d <= 31  or m == 2 and d <= 19:
    print("Acuario")
if m == 2 and d >= 19 and d <= 28 or m == 3 and d <=21:
    print("Piscis")      