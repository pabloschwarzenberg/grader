d = int(input("Ingrese el día de su nacimiento:"))
m = int(input("Ingrese su mes de nacimiento:"))


if d>=21 and m==3 or d<=20 and m==4:
    print("ARIES")
elif d>20 and m==4 or d<=21 and m==5:
    print("TAURO")
elif d>21 and m==5 or d<=21 and m==6:
    print("GEMINIS")
elif d>21 and m==6 or d<=23 and m==7:
    print("CANCER")
elif d>23 and m==7 or d<=23 and m==8:
    print("LEO")
elif d>23 and m==8 or d<=23 and m==9:
    print("VIRGO")
elif d>23 and m==9 or d<=23 and m==10:
    print("LIBRA")
elif d>23 and m==10 or d<=22 and m==11:
    print("ESCORPION")
elif d>22 and m==11 or d<=22 and m==12:
    print("SAGITARIO")
elif d>22 and m==12 or d<=20 and m==1:
    print("CAPRICORNIO")
elif d>20 and m==1 or d<=19 and m==2:
    print("ACUARIO")
elif d>19 and m==2 or d<21 and m==3:
    print("PISCIS")
    