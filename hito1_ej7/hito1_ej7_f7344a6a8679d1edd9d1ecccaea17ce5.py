Dia=int(input("Ingrese su día de nacimiento: "))
M=int(input("Introduce tu mes de nacimiento (1-12): "))
if(Dia>=21 and M==3) or (Dia<=20 and M==4):
    print("aries")
elif(Dia>=21 and M==4) or (Dia<=21 and M==5):
    print("tauro")
elif(Dia>=22 and M==5) or (Dia<=21 and M==6):
    print("geminis")
elif(Dia>=22 and M==6) or (Dia<=22 and M==7):
    print("cancer")
elif(Dia>=23 and M==7) or (Dia<=23 and M==8):
    print("leo")
elif(Dia>=24 and M==8) or (Dia<=23 and M==9):
    print("virgo")
elif(Dia>=24 and M==9) or (Dia<=23 and M==10):
    print("libra")
elif(Dia>=24 and M==10) or (Dia<=22 and M==11):
    print("escorpio")
elif(Dia>=23 and M==11) or (Dia<=21 and M==12):
    print("sagitario")
elif(Dia>=22 and M==12) or (Dia<=20 and M==1):
    print("capricornio")
elif(Dia>=21 and M==1) or (Dia<=18 and M==2):
    print("acuario")
elif(Dia>=19 and M==2) or (Dia<=20 and M==3):
    print("piscis")
      