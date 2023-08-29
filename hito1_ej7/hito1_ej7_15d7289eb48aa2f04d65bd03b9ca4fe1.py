#Zodiaco
dia=int(input("dia en que nacio:"))
mes=int(input("Mes en que nacio: "))

if dia>21 and mes ==3 or dia <= 20 and mes == 4:
    print("usted es aries")
elif dia >= 21 and mes == 4 or dia < 21 and mes == 5:
    print("usted estauro")
elif dia >= 21 and mes == 5 or dia < 2 and mes == 6:
    print("usted es geminis")
elif dia >= 21 and mes == 6 or dia < 23 and mes == 7:
    print("usted es cancer")
elif dia >= 23 and mes == 7 or dia < 23 and mes == 8:
    print("usted es leo")
elif dia >= 23 and mes == 8 or dia < 23 and mes == 9:
    print("usted es virgo")
elif dia >= 23 and mes == 9 or dia < 23 and mes == 10:
    print("usted es libra")
elif dia >= 23 and mes == 10 or dia <= 22 and mes == 11:
    print("usted es escorpio")
elif dia >= 23 and mes == 11 or dia < 22 and mes == 12:
    print("usted es sagitario")
elif dia >= 22 and mes == 12 or dia < 20 and mes == 1:
    print("usted es capricornio")
elif dia >= 20 and mes == 1 or dia < 19 and mes == 2:
    print("usted esacuario")
elif dia >= 19 and mes == 2 or dia < 23 and mes == 3:
    print("usted es piscis")
