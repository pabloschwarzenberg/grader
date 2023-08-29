#Zodiaco
dia=eval(input("Ingrese el dia en que nacio de en forma numerica:"))
mes=eval(input("Ingrese el mes que nacio en forma numerica:"))
if (mes==3 and dia>=21) or (mes==4 and dia<=20):
    print("ARIES")
elif (mes==4 and dia>=20) or (mes==5 and dia<=21):
    print("TAURO")
elif (mes==5 and dia>=21) or (mes==6 and dia<=21):
    print("GEMINIS")
elif (mes==6 and dia>=21) or (mes==7 and dia<=23):
    print("CANCER")
elif (mes==7 and dia >=23) or (mes==8 and dia<=23):
    print("LEON")
elif (mes==8 and dia>=23) or (mes==9 and dia<=23):
    print("VIRGO")
elif (mes==9 and dia>=23) or (mes==10 and dia<=23):
    print("LIBRA")
elif (mes==10 and dia>=23) or (mes==11 and dia<=22):
    print("ESCORPION")
elif (mes==11 and dia>=22) or (mes==12 and dia<=22):
    print("SAGITARIO")
elif (mes==12 and dia>=22) or (mes==1 and dia<=20):
    print("CAPRICORNIO")
elif (mes==1 and dia>=20) or (mes==2 and dia <=19):
    print("ACUARIO")
elif (mes==2 and dia>=19) or (mes==3 and dia<=21):
    print("PISCIS")
   