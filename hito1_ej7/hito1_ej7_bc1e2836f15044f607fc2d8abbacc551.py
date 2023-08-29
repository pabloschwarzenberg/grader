#Zodiaco
d=int(input("Día:"))
m=int(input("Mes:"))
if(20<d and m==3)or(d<21 and m==4):
    print("Aries")
else:
    if(d>20 and m==4)or(d<22 and m==5):
        print("Taurus")
    else:
        if(d>21 and m==5)or(d<22 and m==6):
            print("Gemini")
        else:
            if(d>21 and m==6)or(d<23 and m==7):
                print("Cancer")
            else:
                if(d>22 and m==7)or(d<23 and m==8):
                    print("Leo")
                else:
                    if(d>22 and m==8)or(d<24 and m==9):
                        print("Virgo")
                    else:
                        if(d>23 and m==9)or(d<24 and m==10):
                            print("Libra")
                        else:
                            if(d>23 and m==10)or(d<23 and m==11):
                                print("Scorpio")
                            else:
                                if(d>22 and m==11)or(d<22 and m==12):
                                    print("Sagittarius")
                                else:
                                    if(d>21 and m==12)or(d<19 and m==1):
                                        print("Capricorn")
                                    else:
                                        if(d>20 and m==1)or(d<20 and m==2):
                                            print("Aquarius")
                                        else:
                                            if(d>19 and m==2)or(d<21 and m==3):
                                                print("Pisces")
