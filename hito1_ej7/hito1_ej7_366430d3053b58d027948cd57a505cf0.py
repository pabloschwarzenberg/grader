#Zodiaco
a = int (input ("Ingresa el dia de su cumpleaños: "))
b = int (input ("Ingresa el mes de su cumpleaños: "))
# Proceso

if a>=21 and b==3 or a<=20 and b==4:
    print ("ARIES")
elif a>=21 and b==4 or a<=21 and b==5:
    print ("TAURO")
elif a>=22 and b==5 or a<=21 and b==6:
    print ("GEMINIS")
elif a>=21 and b==6 or a<=23 and b==7:
    print ("CANCER")
elif a>=24 and b==7 or a<=23 and b==8:
    print ("LEON")
elif a>=24 and b==8 or a<=23 and b==9:
    print ("VIRGO")
elif a>=24 and b==9 or a<=23 and b==10:
    print ("LIBRA")
elif a>=24 and b==10 or a<=22 and b==11:
    print ("ESCORPIO")
elif a>=23 and b==11 or a<=21 and b==12:
    print ("SAGITARIO")
elif a>=22 and b==12 or a<=20 and b==1:
    print ("CAPRICORNIO")
elif a>=21 and b==1 or a<=19 and b==2:
    print ("ACUARIO")
elif a>=20 and b==2 or a<=20 and b==3:
    print ("PISCIS")