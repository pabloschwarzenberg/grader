#Zodiaco
dia=int(input("Ingresa el día de tu nacimiento: "))
mes=int(input("Ingresa tu mes de nacimiento entre 1 y 12: "))
if mes==1:
    print("capricornio") if(dia<20) else print("acuario")
if mes==2:
    print("acuario") if(dia<19) else print("piscis")
if mes==3:
    print("piscis") if(dia<21) else print("aries")
if mes==4:
    print("aries") if(dia<20) else print("tauro")
if mes==5:
    print("tauro") if(dia<21) else print("geminis")
if mes==6:
    print("geminis") if(dia<21) else print("leo")
if mes==7:
    print("Tu signo es leo") if(dia<23) else print("virgo")
if mes==8:
    print("virgo") if(dia<23) else print("libra")
if mes==9:
    print("libra") if(dia<23) else print("escorpio")
if mes==10:
    print("Tu signo es escorpio") if(dia<22) else print("sagitario")
if mes==11:
    print("sagitario") if(dia<22) else print("capricornio")
if mes==12:
    print("capricornio")   
    
  