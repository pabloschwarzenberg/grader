#Zodiaco
B=int(input("adjunte su dia de nacimiento: "))
S=int(input("adjunte su mes de nacimiento 1-12: "))
if(B>=21 and S==3) or (B<=20 and S==4):
    print("aries")
elif(B>=21 and S==4) or (B<=21 and S==5):
    print("tauro")
elif(B>=22 and S==5) or (B<=21 and S==6):
    print("geminis")
elif(B>=22 and S==6) or (B<=22 and S==7):
    print("cancer")
elif(B>=23 and S==7) or (B<=23 and S==8):
    print("leo")
elif(B>=24 and S==8) or (B<=23 and S==9):
    print("virgo")
elif(B>=24 and S==9) or (B<=23 and S==10):
    print("libra")
elif(B>=24 and S==10) or (B<=22 and S==11):
    print("escorpio")
elif(B>=23 and S==11) or (B<=21 and S==12):
    print("sagitario")
elif(B>=22 and S==12) or (B<=20 and S==1):
    print("capricornio")
elif(B>=21 and S==1) or (B<=18 and S==2):
    print("acuario")
elif(B>=19 and S==2) or (B<=20 and S==3):
    print("piscis")