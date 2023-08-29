#Zodiaco
X=int(input("introduce el dia de nacimiento: "))
Y=int(input("introduce el mes de nacimiento 1-12: "))
if(X>=21 and Y==3) or (X<=20 and Y==4):
    print("aries")
elif(X>=21 and Y==4) or (X<=21 and Y==5):
    print("tauro")
elif(X>=22 and Y==5) or (X<=21 and Y==6):
    print("geminis")
elif(X>=22 and Y==6) or (X<=22 and Y==7):
    print("cancer")
elif(X>=23 and Y==7) or (X<=23 and Y==8):
    print("leo")
elif(X>=24 and Y==8) or (X<=23 and Y==9):
    print("virgo")
elif(X>=24 and Y==9) or (X<=23 and Y==10):
    print("libra")
elif(X>=24 and Y==10) or (X<=22 and Y==11):
    print("escorpio")
elif(X>=23 and Y==11) or (X<=21 and Y==12):
    print("sagitario")
elif(X>=22 and Y==12) or (X<=20 and Y==1):
    print("capricornio")
elif(X>=21 and Y==1) or (X<=18 and Y==2):
    print("acuario")
elif(X>=19 and Y==2) or (X<=20 and Y==3):
    print("piscis")      