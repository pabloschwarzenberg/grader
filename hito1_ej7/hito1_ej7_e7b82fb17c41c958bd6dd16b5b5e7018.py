#Zodiaco
dia=int(input("ingrese el dia de nacimiento: "))
mes=int(input("ingrese el mes de nacimiento: "))
if((mes==3 and dia>21 and dia<=31) or (mes==4 and dia>=1 and dia<=20)):
   print("ARIES")
elif((mes==4 and dia>20 and dia<=30) or (mes==5 and dia>=1 and dia<=21)):
    print("TAURO")
elif((mes==5 and dia>21 and dia<=31) or (mes==6 and dia>=1 and dia<=21)):
    print("GEMINIS")
elif((mes==6 and dia>21 and dia<=30) or (mes==7 and dia>=1 and dia<=23)):
    print("CANCER")
elif((mes==7 and dia>23 and dia<=30) or (mes==8 and dia>=1 and dia<=23)):
    print("LEO")
elif((mes==8 and dia>23 and dia<=31) or (mes==9 and dia>=1 and dia<=23)):
    print("VIRGO")
elif((mes==9 and dia>23 and dia<=30) or (mes==10 and dia>=1 and dia<=23)):
     print("LIBRA")
elif((mes==10 and dia>23 and dia<=31) or(mes==11 and dia>=1 and dia<=22)):
    print("ESCORPION")
elif((mes==11 and dia>22 and dia<=30) or (mes==12 and dia>=1 and dia<=22)):
     print("SAGITARIO")
elif((mes==12 and dia>22 and dia<=31) or (mes==1 and dia>=1 and dia<=20)):
    print("CAPRICORNIO")
elif((mes==1 and dia>20 and dia<=31) or (mes==2 and dia>=1 and dia<=19)):
    print("ACUARIO")
elif((mes==2 and dia>19 and dia<=28) or (mes==3 and dia>=1 and dia<=21)):
    print("PISCIS")      