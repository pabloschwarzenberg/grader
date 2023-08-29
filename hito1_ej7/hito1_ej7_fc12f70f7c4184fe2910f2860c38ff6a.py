#Zodiaco
dia=int(input("ingrese el dia en que nacio: "))
mes=int(input("ingrese el mes en que nacio: "))
if int(mes)==3 and dia>=21 and dia<=31 or int(mes)==4 and dia>=1 and dia<=20:
    print("ARIES")
elif int(mes)==4 and dia>=20 and dia<=30 or int(mes)==5 and dia>=1 and dia<=21:
    print("TAURO")
elif int(mes)==5 and dia>=21 and dia<=31 or int(mes)==6 and dia>=1 and dia<=21:
    print("GEMINIS")
elif int(mes)==6 and dia>=21 and dia<=30 or int(mes)==7 and dia>=1 and dia<=23:
    print("CANCER")
elif int(mes)==7 and dia>=23 and dia<=31 or int(mes)==8 and dia>=1 and dia<=23:
    print("LEO")
elif int(mes)==8 and dia>=23 and dia<=31 or int(mes)==9 and dia>=1 and dia<=23:
    print("VIRGO")
elif int(mes)==9 and dia>=23 and dia<=30 or int(mes)==10 and dia>=1 and dia<=23:
    print("LIBRA")
elif int(mes)==10 and dia>=23 and dia<=31 or int(mes)==11 and dia>=1 and dia<=22:
    print("ESCORPION")
elif int(mes)==11 and dia>=22 and dia<=30 or int(mes)==12 and dia>=1 and dia<=22:
    print("SAGITARIO")
elif int(mes)==12 and dia>=22 and dia<=31 or int(mes)==1 and dia>=1 and dia<=20:
    print("CAPRICORNIO")
elif int(mes)==1 and dia>=20 and dia<=31 or int(mes)==2 and dia>=1 and dia<=19:
    print("ACUARIO")
elif int(mes)==2 and dia>=19 and dia<=29 or int(mes)==3 and dia>=1 and dia<=21:
    print("PISCIS")