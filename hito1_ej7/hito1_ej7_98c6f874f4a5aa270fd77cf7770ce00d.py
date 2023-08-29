d=int(input("Dia:"))
m=int(input("Mes:"))

if d>=21 and d<=31 and m==3 or d>=1 and d<=20 and m==4:
    print("su signo es aries")
elif d>20 and d<=30 and m==4 or d>=1 and d<=21 and m==5:
    print("su signo es tauro")
elif d>21 and d<=31 and m==5 or d>=1 and d<=21 and m==6:
    print("su signo es gemini")
elif d>21 and d<=30 and m==6 or d>=1 and d<=23 and m==7:
    print("su signo es cancer")
elif d>23 and d<=31 and m==7 or d>=1 and d<=23 and m==8:
    print("su signo es leo")
elif d>23 and d<=31 and m==8 or d>=1 and d<=23 and m==9:
    print("su signo es virgo")
elif d>23 and d<=30 and m==9 or d>=1 and d<=23 and m==10:
    print("su signo es libra")
elif d>23 and d<=31 and m==10 or d>=1 and d<=23 and m==11:
    print("su signo es escorpio")
elif d>22 and d<=30 and m==11 or d>=1 and d<=22 and m==12:
   print("su signo es sagitario")
elif d>22 and d<=31 and m==12 or d>=1 and d<=20 and m==1:
    print("su signo es capricornio")
elif d>20 and d<=31 and m==1 or d>=1 and d<=19 and m==2:
    print("su signo es acuario")
elif d>19 and d<=28 and m==2 or d>=1 and d<=21 and m==3:
    print("su signo es piscis")
