#Zodiaco
D=int(input("Ingrese su día de nacimiento:"))
M=int(input("Ingrese su mes de nacimiento:"))
if(D>=21 and M==3) or (D<=20 and M==4):
    print("aries")
elif(D>=21 and M==4) or (D<=21 and M==5):
    print("tauro")
elif(D>=22 and M==5) or (D<=21 and M==6):
    print("geminis")
elif(D>=22 and M==6) or (D<=22 and M==7):
    print("cancer")
elif(D>=23 and M==7) or (D<=23 and M==8):
    print("leo")
elif(D>=24 and M==8) or (D<=23 and M==9):
    print("virgo")
elif(D>=24 and M==9) or (D<=23 and M==10):
    print("libra")
elif(D>=24 and M==10) or (D<=22 and M==11):
    print("escorpio")
elif(D>=23 and M==11) or (D<=21 and M==12):
    print("sagitario")
elif(D>=22 and M==12) or (D<=20 and M==1):
    print("capricornio")
elif(D>=21 and M==1) or (D<=18 and M==2):
    print("acuario")
elif(D>=19 and M==2) or (D<=20 and M==3):
    print("piscis")