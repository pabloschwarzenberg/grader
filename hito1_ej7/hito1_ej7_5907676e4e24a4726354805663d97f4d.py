#Zodiaco
print("inserte dia de nacimiento: ")
d = eval(input())
print("inserte mes de nacimiento: ")
m = eval(input())
if (d>=21 or d<=20 and m==3 or m==4):
    print("aries")
if (d>=20 or d<=21 and m==4 or m==5):
    print("tauro")
if (d>=21 or d<=21 and m==5 or m==6):
    print("gemini")
if (d>=21 or d<=23 and m==6 or m==7):
    print("cancer")
if (d>=23 or d<=23 and m==7 or m==8):
    print("leo")
if (d>=23 or d<=23 and m==8 or m==9):
    print("virgo")
if (d>=23 or d<=23 and m==9 or m==10):
    print("libra")
if (d>=23 or d<=22 and m==10 or m==11):
    print("scorpio")
if (d>=22 or d<=22 and m==11 or m==12):
    print("sagitario")
if (d>=22 or d<=20 and m==12 or m==1):
    print("capricornio")
if (d>=20 or d<=19 and m==1 or m==2):
    print("aquario")
if (d>=19 or d<=21 and m==2 or m==3):
    print("piscis")