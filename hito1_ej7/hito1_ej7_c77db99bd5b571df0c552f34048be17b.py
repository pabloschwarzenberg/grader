#Zodiaco
d = int(input("dia ->"))
m = int(input("mes ->"))

if d>=21 and m==3 or d<=20 and m==4:
     print("Su signo es Aries")
elif d>20 and m==4 or d<=21 and m==5:
     print("Su signo es Tauro")
elif d>21 and m==4 or d<=21 and m==6:
     print("Su signo es Gemenis")
elif d>21 and m==6 or d<=23 and m==7:
     print("Su signo es Cancer")
elif d>23 and m==6 or d<=23 and m==7:
     print("Su signo es Leo")
elif d>23 and m==8 or d<=23 and m==9:
     print("Su signo es Virgo")
elif d>23 and m==9 or d<=23 and m==10:
     print("Su signo es Libra")
elif d>23 and m==10 or d<=23 and m==11:
     print("Su signo es Escorpio")
elif d>22 and m==11 or d<=22 and m==12:
     print("Su signo es Sagitario")
elif d>22 and m==12 or d<=20 and m==1:
     print("Su signo es Capricornio")
elif d>20 and m==1 or d<=19 and m==2:
    print("Su signo es Acuario")
elif d>2 and m==2 or d<=21 and m==3:
    print("Su signo es Piscis")