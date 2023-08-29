#Zodiaco

d=int(input("Dia en el que nacio : "))
m=int(input("Mes de nacimiento (ej: si es mayo, ingrese 5): "))




if ((m==3 and d>=21) or (m==4 and d <=20)):
    print("ARIES")

elif ((m==4 and d>=21) or (m==5 and d <=20)):
    print("TAURO")

elif ((m==5 and d>=21) or (m==6 and d <=20)):
    print("GEMINIS")

elif ((m==6 and d>=21) or (m==7 and d <=21)):
    print("CANCER")

elif ((m==7 and d>=22) or (m==8 and d <=22)):
    print("LEO")

elif ((m==8 and d>=23) or (m==9 and d <=22)):
    print("VIRGO")

elif ((m==9 and d>=23) or (m==10 and d <=22)):
    print("LIBRA")

elif ((m==10 and d>=23) or (m==11 and d <=21)):
    print("ESCORPIO")

elif ((m==11 and d>=22) or (m==12 and d <=21)):
    print("SAGITARIO")

elif ((m==12 and d>=22) or (m==1 and d <=19)):
    print("CAPRICORNIO")

elif ((m==1 and d>=20) or (m==2 and d <=18)):
    print("ACUARIO")

elif ((m==2 and d>=19) or (m==2 and d <=21)):
    print("PISCIS")
