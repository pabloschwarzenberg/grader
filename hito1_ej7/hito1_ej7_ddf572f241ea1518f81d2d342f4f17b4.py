#Zodiaco
DN = int(input("¿En qué día nació?:"))
MN= int(input("Número de mes en que nació:"))
if DN > 21 and MN == 3 or MN == 4 and DN <= 20:
    print("usted es aries")
if DN > 20 and MN == 4 or MN == 5 and DN <= 21:
    print("usted es tauro")
if DN > 21 and MN == 5 or MN == 6 and DN <= 21:
    print("usted es géminis")
if DN > 21 and MN == 6 or MN == 7 and DN <= 23:
    print("usted es cáncer")
if DN > 23 and MN == 7 or MN == 8 and DN <= 23:
    print("usted es leo")
if DN > 23 and MN == 8 or MN == 9 and DN <= 23:
    print("usted es virgo")
if DN > 23 and MN == 9 or MN == 10 and DN <= 23:
    print("usted es libra")
if DN > 23 and MN == 10 or MN == 11 and DN <= 22:
    print("usted es escorpio")
if DN > 22 and MN == 11 or MN == 12 and DN <= 22:
    print("usted es sagitario")
if DN > 22 and MN == 12 or MN == 1 and DN <= 20:
    print("usted es capricornio")
if DN > 20 and MN == 1 or MN == 2 and DN <= 19:
    print("usted es acuario")
if DN > 19 and MN == 2 or MN == 3 and DN <= 21:
    print("usted es piscis")