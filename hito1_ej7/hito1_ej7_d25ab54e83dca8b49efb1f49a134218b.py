dia=int(input("ingrese su dia de nacimiento: "))
meses=int(input("ingrese su mes de nacimiento : "))
if(dia>=21 and meses==3) or (dia<=20 and meses==4):
    print("aries")
elif(dia>=21 and meses==4) or (dia<=21 and meses==5):
    print("tauro")
elif(dia>=22 and meses==5) or (dia<=21 and meses==6):
    print("geminis")
elif(dia>=22 and meses==6) or (dia<=22 and meses==7):
    print("cancer")
elif(dia>=23 and meses==7) or (dia<=23 and meses==8):
    print("leo")
elif(dia>=24 and meses==8) or (dia<=23 and meses==9):
    print("virgo")
elif(dia>=24 and meses==9) or (dia<=23 and meses==10):
    print("libra")
elif(dia>=24 and meses==10) or (dia<=22 and meses==11):
    print("escorpio")
elif(dia>=23 and meses==11) or (dia<=21 and meses==12):
    print("sagitario")
elif(dia>=22 and meses==12) or (dia<=20 and meses==1):
    print("capricornio")
elif(dia>=21 and meses==1) or (dia<=18 and meses==2):
    print("acuario")
elif(dia>=19 and meses==2) or (dia<=20 and meses==3):
    print("piscis")
