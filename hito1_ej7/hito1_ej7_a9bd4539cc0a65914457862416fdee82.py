#Zodiaco
d = int(input("escriba el dia en el que nacio como numero"))
m = int(input("escriba el mes en el que nacio como numero"))
if 21<= d <=31 and m==3 or 1<= d <20 and m==4:
    print("aries")
else:
    if 20<= d <=30 and m==4 or 1<= d <21 and m==5:
        print("tauro")
    else:
        if 21<= d <=31 and m==5 or 1<= d <21 and m==6:
            print("geminis")
        else:
            if 21<= d <=31 and m==6 or 1<= d <23 and m==7:
                print("cancer")
            else:
                if 23<= d <=31 and m==7 or 1<= d <23 and m==8:
                    print("leo")
                else:
                    if 23<= d <=31 and m==8 or 1<= d <23 and m==9:
                        print("virgo")
                    else:
                        if 23<= d <=30 and m==9 or 1<= d <23 and m==10:
                            print("libra")
                        else:
                            if 23<= d <=31 and m==10 or 1<= d <22 and m==11:
                                print("escorpio")
                            else:
                                if 22<= d <=30 and m==11 or 1<= d <22 and m==12:
                                    print("sagitario")
                                else:
                                    if 22<= d <=31 and m==12 or 1<= d <20 and m==1:
                                        print("capricornio")
                                    else:
                                        if 20<= d <=31 and m==1 or 1<= d <19 and m==2:
                                            print("acuario")
                                        else:
                                            print("piscis")