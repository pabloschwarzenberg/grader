#Zodiaco

dia=int(input("Día: "))
mes=int(input("Mes: "))

if (21<=dia<=31 and mes==3) or (0<dia<=20 and mes==4):
    print("Aries")
elif (21<=dia<=31 and mes==4) or (0<dia<=21 and mes==5):
    print("Taurus")
elif (22<=dia<=31 and mes==5) or (0<dia<=21 and mes==6):
    print("Gemini")
elif (22<=dia<=31 and mes==6) or (0<dia<=22 and mes==7):
    print("Cancer")
elif (23<=dia<=31 and mes==7) or (0<dia<=22 and mes==8):
    print("Leo")
elif (23<=dia<=31 and mes==8) or (0<dia<=23 and mes==9):
    print("Virgo")
elif (24<=dia<=31 and mes==9) or (0<dia<=23 and mes==10):
    print("Libra")
elif (24<=dia<=31 and mes==10) or (0<dia<=22 and mes==11):
    print("Scorpio")
elif (23<=dia<=31 and mes==11) or (0<dia<=21 and mes==12):
    print("Sagittarius")
elif (22<=dia<=31 and mes==12) or (0<dia<=20 and mes==1):
    print("Capricorn")
elif (21<=dia<=31 and mes==1) or (0<dia<=19 and mes==2):
    print("Aquarius")
elif (20<=dia<=31 and mes==2) or (0<dia<=20 and mes==3):
    print("Pisces")