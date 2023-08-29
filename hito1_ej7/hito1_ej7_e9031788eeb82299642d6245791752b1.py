#Zodiaco
d = int(input("ingrese el dia de su nacimiento : "))
m = int(input("ingrese el numero del mes en el que nacio : "))
if m == 3 and d >= 21 and d <=31 or m == 4 and d >= 1 and d <= 20:
    print("aries")
else:
    if m == 4 and d >= 20 and d <= 30 or m == 5 and d >= 1 and d <= 20:
        print("tauro")
    else:
        if m == 5 and d >= 21 and d <= 31 or m == 6 and d >= 1 and d <= 20:
            print("geminis")
        else:
            if m == 6 and d >= 21 and d <= 30 or m == 7 and d >= 1 and d <= 22:
                print("cancer")
            else:
                if m == 7 and d >= 23 and d <= 31 or m == 8 and d >= 1 and d <= 22:
                    print("leo")
                else:
                    if m == 8 and d >= 23 and d <= 31 or m == 9 and d >= 1 and d <= 22:
                        print("virgo")
                    else:
                        if m == 9 and d >= 23 and d <= 30 or m == 10 and d >= 1 and d <= 22:
                            print("libra")
                        else:
                            if m == 10 and d >= 23 and d <= 31 or m == 11 and d >= 1 and d <= 21:
                                print("escorpio")
                            else:
                                if m == 11 and d >= 22 and d <= 30 or m == 12 and d >= 1 and d <= 21:
                                    print("sagitario")
                                else:
                                    if m == 12 and d >= 22 and d <= 30 or m == 1 and d >= 1 and d <= 19:
                                        print("capricornio")
                                    else:
                                        if m == 1 and d >= 20 and d <= 31 or m == 2 and d >= 1 and d <= 18:
                                            print("acuario")
      