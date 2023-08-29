#Zodiaco
d=int(input("Ingrese el dia de su cumpleaños: "))
m=int(input("Ingrese el mes de su cumpleaños: "))
if (21<=d<=31 and m==3) or (1<=d<20 and m==4):
    print("Eres Aries")
elif  (20<=d<=31 and m==4) or (1<=d<21 and m==5):
    print("Eres Tauro")
elif (21<=d<=31 and m==5) or (1<=d<21 and m==6):
    print("Eres Geminis")
elif  (21<=d<=31 and m==6) or (1<=d<23 and m==7):
    print("Eres Cancer")
elif (23<=d<=31 and m==7) or (1<=d<23 and m==8):
    print("Eres Leo")
elif (23<=d<=31 and m==8) or (1<=d<23 and m==9):
    print("Eres Virgo")
elif (23<=d<=31 and m==9) or (1<=d<23 and m==10):
    print("Eres Libra")
elif (23<=d<=31 and m==10) or (1<=d<22 and m==11):
    print("Eres Escorpión")
elif (22<=d<=31 and m==11) or (1<=d<22 and m==12):
    print("Eres Sagitario")
elif (22<=d<=31 and m==12) or (1<=d<20 and m==1):
    print("Eres Capricornio")
elif (20<=d<=31 and m==1) or (1<=d<19 and m==2):
    print("Eres Acuario")
elif (19<=d<=31 and m==2) or (1<=d<21 and m==3):
    print("Eres Piscis")      