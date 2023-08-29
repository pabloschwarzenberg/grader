#Zodiaco
print("para saber su signo zodiacal ingrese: ")
d=int(input("dia de nacimiento: "))
m=int(input("mes de nacimiento: "))
if (21<=d<=31 or 1<=d<=20) and (m==3 or m==4):
    print("aries")
elif (21<=d<=30 or 1<=d<=20) and (m==4 or m==5):
    print("tauro")
elif (21<=d<=31 or 1<=d<=21) and (m==5 or m==6):
    print("geminis")
elif (22<=d<=30 or 1<=d<=21) and (m==6 or m==7):
    print("cancer")
elif (22<=d<=31 or 1<=d<=23) and (m==7 or m==8):
    print("leo")
elif (24<=d<=31 or 1<=d<=23) and (m==8 or m==9):
    print("virgo")
elif (24<=d<=30 or 1<=d<=22) and (m==9 or m==10):
    print("libra")
elif (23<=d<=31 or 1<=d<=22) and (m==10 or m==11):
    print("escorpio")
elif (23<=d<=30 or 1<=d<=21) and (m==11 or m==12):
    print("sagitario")
elif (22<=d<=31 or 1<=d<=20) and (m==12 or m==1):
    print("capricornio")
elif (21<=d<=31 or 1<=d<=19) and (m==1 or m==2):
    print("acuario")
elif (20<=d<=28 or 1<=d<=20) and (m==2 or m==3):
    print("piscis")