#Zodiaco
S=int(input("adjunte su dia de nacimiento: "))
Z=int(input("adjunte su mes de nacimiento 1-12: "))
if(S>=21 and Z==3) or (S<=20 and Z==4):
    print("aries")
elif(S>=21 and Z==4) or (S<=21 and Z==5):
    print("tauro")
elif(S>=22 and Z==5) or (S<=21 and Z==6):
    print("geminis")
elif(S>=22 and Z==6) or (S<=22 and Z==7):
    print("cancer")
elif(S>=23 and Z==7) or (S<=23 and Z==8):
    print("leo")
elif(S>=24 and Z==8) or (S<=23 and Z==9):
    print("virgo")
elif(S>=24 and Z==9) or (S<=23 and Z==10):
    print("libra")
elif(S>=24 and Z==10) or (S<=22 and Z==11):
    print("escorpio")
elif(S>=23 and Z==11) or (S<=21 and Z==12):
    print("sagitario")
elif(S>=22 and Z==12) or (S<=20 and Z==1):
    print("capricornio")
elif(S>=21 and Z==1) or (S<=18 and Z==2):
    print("acuario")
elif(S>=19 and Z==2) or (S<=20 and Z==3):
    print("piscis")
