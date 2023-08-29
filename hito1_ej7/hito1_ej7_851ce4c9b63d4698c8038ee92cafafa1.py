a = eval(input("Dia"))
b = eval(input("mes"))

ari = (a > 21 and b == 3) or (a <= 20 and b == 4)
tau = (a > 20 and b == 4) or (a <= 21 and b == 5)
gem = (a > 21 and b == 5) or (a <= 21 and b == 6)
can = (a > 21 and b == 6) or (a <= 23 and b == 7)
leo = (a > 23 and b == 7) or (a <= 23 and b == 8)
vir = (a > 23 and b == 8) or (a <= 23 and b == 9)
lib = (a > 23 and b == 9) or (a <= 23 and b == 10)
sco = (a > 23 and b == 10) or (a <= 22 and b == 11)
sag = (a > 22 and b == 11) or (a <= 22 and b == 12)
cap = (a > 22 and b == 12) or (a <= 20 and b == 1)
acu = (a > 20 and b == 1) or (a <= 19 and b == 2)
pis = (a > 19 and b == 2) or (a <= 21 and b == 3)

if ari == True:
    print("Aries")
else:
    if tau == True:
        print("Tauro")
    else:
        if gem == True:
            print("Geminis")
        else:
            if can == True:
                print("Cancer")
            else:
                if leo == True:
                    print("Leo")
                else:
                    if vir == True:
                        print("Virgo")
                    else:
                        if lib == True:
                            print("Libra")
                        else:
                            if sco == True:
                                print("Escorpio")
                            else:
                                if sag == True:
                                    print("Sagitario")
                                else:
                                    if cap == True:
                                        print("Capricornio")
                                    else:
                                        if acu == True:
                                            print("Acuario")
                                        else:
                                            if pis == True:
                                                print("Piscis")