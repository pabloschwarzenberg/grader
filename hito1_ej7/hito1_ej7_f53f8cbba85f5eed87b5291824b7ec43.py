#Zodiaco
#"Para Saber Tu Signo"
d=int(input("Dia:"))
m=int(input("Mes:"))

if d>=21 and m==3 or d<=20 and m==4:
    print("aries")
elif d>20 and m==4 or d<=21 and m==5:
    print("tauro")
elif d>21 and m==4 or d<=21 and m==6:
    print("geminis")
elif d>21 and m==6 or d>=23 and m==7:
    print("cancer")
elif d>23 and m==6 or d<=23 and m==8:
    print("leo")
elif d>23 and m==8 or d<=23 and m==9:
    print("virgo")
elif d>23 and m==9 or d<=23 and m==10:
    print("libra")
elif d>23 and m==10 or d<=23 and m==11:
    print("escorpio")
elif d>22 and m==11 or d<=22 and m==12:
    print("sagitario")
elif d>22 and m==12 or d<=20 and m==1:
    print("capricornio")
elif d>20 and m==1 or d<=19 and m==2:
    print("acuario")
elif d>19 and m==2 or d<=21 and m==3:
    print("piscis")
