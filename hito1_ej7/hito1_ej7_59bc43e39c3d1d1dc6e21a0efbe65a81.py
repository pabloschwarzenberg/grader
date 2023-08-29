#Zodíaco
D = int(input("Día de su cumpleaños: "))
M = int(input("Mes de su cumpleaños (Representar los meses con números del 1 al 12): "))
if (D > 21 and D <=31 and M == 3) or ( D >= 1 and D <=20  and M ==4):
    print("Aries")
elif (D >= 21 and D <= 31 and M == 4) or (D >= 1 and D <= 21 and M == 5):
        print("Tauro")
elif (D > 21 and D <= 31 and M == 5) or (D >= 1 and D <= 21 and M == 6):
            print("Geminis")
elif (D > 21 and D <= 31 and M == 6) or (D >= 1 and D <= 23 and M == 7):
                print("Cancer")
elif (D > 23 and D <= 31 and M == 7) or (D >= 1 and D <= 23 and M == 8):
                    print("Leo")
elif (D > 23 and D <= 31 and M == 8) or (D >= 1 and D <= 23 and M == 9):
                        print("Virgo")
elif (D > 23 and D <= 31 and M == 9) or (D >= 1 and D <= 23 and M == 10):
                            print("Libra")
elif (D > 23 and D <= 31 and M == 10) or (D >= 1 and D <= 22 and M == 11):
                                print("Escorpio")
elif (D > 22 and D <= 31 and M == 11) or (D >= 1 and D <= 22 and M == 12):
                                    print("Sagitario")
elif (D > 2 and D <= 31 and M == 12) or (D >= 1 and D <= 20 and M == 1):
                                        print("Capricornio")
elif (D > 20 and D <= 31 and M == 1) or (D >= 1 and D <= 19 and M == 2):
                                            print("Acuario")
elif (D > 19 and D <= 31 and M == 2) or (D >= 1 and D <= 21 and M == 3):
                                                print("Piscis")
      