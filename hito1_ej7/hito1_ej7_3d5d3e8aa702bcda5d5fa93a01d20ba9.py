#Zodiaco
dia=int(input("Ingrese su día de cumpleaños: "))
mes=int(input("Ingrese su mes de cumpleaños en número: "))

if 21<=dia<=31 and mes==3 or 1<=dia<=20 and mes==4:
    print("VIRGO")
    
elif 21<=dia<=30 and mes==4 or 1<=dia<=21 and mes==5:
    print("TAURO")
    
elif 22<=dia<=31 and mes==5 or 1<=dia<=21 and mes==6:
    print("GEMINIS")

elif 22<=dia<=30 and mes==6 or 1<=dia<=22 and mes==7:
    print("CÁNCER")

elif 23<=dia<=31 and mes==7 or 1<=dia<=22 and mes==8:
    print("LEÓN")
    
elif 23<=dia<=31 and mes==8 or 1<=dia<=23 and mes==9:
    print("VIRGO")
    
elif 24<=dia<=30 and mes==9 or 1<=dia<=23 and mes==10:
    print("LIBRA")

elif 24<=dia<=31 and mes==10 or 1<=dia<=22 and mes==11:
    print("ESCORPIÓN")

elif 23<=dia<=30 and mes==11 or 1<=dia<=21 and mes==12:
    print("SAGITARIO")

elif 22<=dia<=31 and mes==12 or 1<=dia<=20 and mes==1:
    print("CAPRICORNIO")

elif 21<=dia<=31 and mes==1 or 1<=dia<=19 and mes==2:
    print("ACUARIO")

elif 20<=dia<=28 and mes==2 or 1<=dia<=20 and mes==3:
    print("PISCIS")

else:
    print("NO EXISTE")


      