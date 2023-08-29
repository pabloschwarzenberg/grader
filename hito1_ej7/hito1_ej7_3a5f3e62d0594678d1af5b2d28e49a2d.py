#Zodiaco
d=int(input())
m=int(input())
if 21<=d and m==3 or d<=20 and m==4:
    print("aries")
if 21<=d and m==4 or d<=21 and m==5:
    print("tauro")
if 22<=d and m==5 or d<=21 and m==6:
    print("geminis")
if 22<=d and m==6 or d<=22 and m==7:
    print("cancer")
if 23<=d and m==7 or d<=22 and m==8:
    print("leo")
if m==8 and d>=23 or m==9 and d<=23:
    print("virgo")
if 24<=d and m==9 or d<=23 and m==10:
    print("libra")
if 24<=d and m==10 or d<=22 and m==11:
    print("scorpio")
if 23<=d and m==11 or d<=21 and m==12:
    print("sagitario")
if 22<=d and m==12 or d<=20 and m==1:
    print("capricornio")
if 21<=d and m==1 or d<=19 and m==2:
    print("acuario")
if 20<=d and m==2 or d<=20 and m==3:
    print("Pisces")
