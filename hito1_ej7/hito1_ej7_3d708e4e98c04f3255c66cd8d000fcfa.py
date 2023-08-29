day = int(input())
mon = int(input())

if day >= 20 and mon == 1 or day < 19 and mon == 2:
    print("acuario")
elif day >= 19 and mon == 2 or day < 21 and mon == 3:
    print("piscis")
elif day >= 21 and mon == 3 or day < 20 and mon == 4:
    print("aries")
elif day >= 20 and mon == 4 or day < 21 and mon == 5:
    print("tauro")
elif day >= 21 and mon == 5 or day < 21 and mon == 6:
    print("geminis")
elif day >= 21 and mon == 6 or day < 23 and mon == 7:
    print("cancer")
elif day >= 23 and mon == 7 or day < 23 and mon == 8:
    print("leo")
elif day >= 23 and mon == 8 or day < 23 and mon == 9:
    print("virgo")
elif day >= 23 and mon == 9 or day < 23 and mon == 10:
    print("libra")
elif day >= 23 and mon == 10 or day < 22 and mon == 11:
    print("escorpio")
elif day >= 23 and mon == 11 or day < 22 and mon == 12:
    print("sagitario")
elif day >= 22 and mon == 12 or day < 20 and mon == 1:
    print("capricornio")